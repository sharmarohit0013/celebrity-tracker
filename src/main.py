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

            # 🔽 Custom INSERT from user
            choice = input("Do you want to insert a new celebrity? (y/n): ").lower()
            if choice == 'y':
                name = input("Enter celebrity name: ")
                profession = input("Enter profession: ")
                birthdate = input("Enter birthdate (YYYY-MM-DD): ")
                bio = input("Enter bio: ")
                DataInserter(cur).insert_celebrity(name, profession, birthdate, bio)
                print("✅ Celebrity inserted.")

            # 🔽 Custom UPDATE from user
            choice = input("Do you want to update a celebrity's bio? (y/n): ").lower()
            if choice == 'y':
                celeb_id = int(input("Enter celebrity ID to update: "))
                new_bio = input("Enter new bio: ")
                DataUpdater(cur).update_celeb_bio(celeb_id, new_bio)
                print(f"✅ Updated bio for celebrity ID {celeb_id}.")

            # 🔽 Custom DELETE from user
            choice = input("Do you want to delete a celebrity? (y/n): ").lower()
            if choice == 'y':
                celeb_id = int(input("Enter celebrity ID to delete: "))
                DataDeleter(cur).delete_celeb_by_id(celeb_id)
                print(f"🗑️ Deleted celebrity with ID {celeb_id}.")

            # 🔽 Fetch celebrity by partial name
            choice = input("Do you want to search celebrities by name? (y/n): ").lower()
            if choice == 'y':
                partial_name = input("Enter partial/full celebrity name: ")
                results = DataFetcher(cur).individual_celeb(partial_name)
                if results:
                    print("\n🎬 Search Results:")
                    for celeb in results:
                        print(f"  ID: {celeb[0]}, Name: {celeb[1]}, Profession: {celeb[2]}, Birthdate: {celeb[3]}, Bio: {celeb[4]}")
                else:
                    print("⚠️ No celebrities found matching that name.")

            # Fetch all data
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
    