import psycopg2
import time

DB_CONFIG = {
    "dbname": "celebdb",
    "user": "celebuser",
    "password": "celebpass",
    "host": "db",
    "port": "5432"
}

def create_tables_insert_and_fetch():
    for i in range(10):
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            print("✅ Connected to PostgreSQL!")

            cur = conn.cursor()

            # 1. Create tables
            cur.execute("""
                CREATE TABLE IF NOT EXISTS CelebDetails (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    profession TEXT,
                    birthdate DATE,
                    bio TEXT
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS "user" (
                    id SERIAL PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            print("✅ Tables created.")

            # 2. Insert sample data
            cur.execute("""
                INSERT INTO CelebDetails (name, profession, birthdate, bio)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT DO NOTHING;
            """, ("Robert Downey Jr.", "Actor", "1965-04-04", "Plays Iron Man in Marvel movies."))

            # cur.execute("""
            #     INSERT INTO "user" (username, email, password)
            #     VALUES (%s, %s, %s)
            #     ON CONFLICT (username, email) DO NOTHING;
            # """, ("admin", "admin@example.com", "admin123"))

            conn.commit()
            print("✅ Sample data inserted.")

            # 3. Fetch and display data from CelebDetails
            print("\n🎬 CelebDetails Table:")
            cur.execute("SELECT id, name, profession, birthdate, bio FROM CelebDetails;")
            celebs = cur.fetchall()
            for celeb in celebs:
                print(f"  ID: {celeb[0]}, Name: {celeb[1]}, Profession: {celeb[2]}, Birthdate: {celeb[3]}, Bio: {celeb[4]}")

            # # 4. Fetch and display data from user table
            # print("\n👤 User Table:")
            # cur.execute('SELECT id, username, email, created_at FROM "user";')
            # users = cur.fetchall()
            # for user in users:
            #     print(f"  ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Created At: {user[3]}")

            # Close resources
            cur.close()
            conn.close()
            break

        except Exception as e:
            print(f"⏳ Attempt {i+1}: Waiting for DB... ({e})")
            time.sleep(2)
    else:
        print("❌ Could not connect after retries.")

if __name__ == "__main__":
    create_tables_insert_and_fetch()