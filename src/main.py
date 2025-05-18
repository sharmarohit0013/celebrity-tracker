import time
from db.connection import get_connection
from db.models import TableManager
from db.insert import DataInserter
from db.fetch import DataFetcher

def main():
    for i in range(10):
        try:
            conn = get_connection()
            print("✅ Connected to PostgreSQL!")
            cur = conn.cursor()

            TableManager(cur).create_tables()
            print("✅ Tables created.")

            DataInserter(cur).insert_sample_data()
            print("✅ Sample data inserted.")

            celebs = DataFetcher(cur).fetch_celebs()
            print("\n🎬 CelebDetails Table:")
            for c in celebs:
                print(f"  ID: {c[0]}, Name: {c[1]}, Profession: {c[2]}, Birthdate: {c[3]}, Bio: {c[4]}")

            conn.commit()
            cur.close()
            conn.close()
            print("🔒 Connection closed.")
            break

        except Exception as e:
            print(f"⏳ Attempt {i+1}: Waiting for DB... ({e})")
            time.sleep(2)
    else:
        print("❌ Could not connect after retries.")

if __name__ == "__main__":
    main()
