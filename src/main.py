import time
from db.connection import get_connection
from db.models import TableManager
from db.insert import DataInserter
from db.fetch import DataFetcher
from db.update import DataUpdater
from db.delete import DataDeleter

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

            # Update example
            DataUpdater(cur).update_celeb_bio(1, "Updated bio for RDJ")
            print("✅ Celeb bio updated.")

            # Delete example
            DataDeleter(cur).delete_celeb_by_id(1)
            print("🗑️ Deleted celeb with ID 1")

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
