import psycopg2
import time


class PostgresManager:
    def __init__(self, db_config, retries=10, delay=2):
        self.db_config = db_config
        self.retries = retries
        self.delay = delay
        self.conn = None
        self.cur = None

    def connect(self):
        for i in range(self.retries):
            try:
                self.conn = psycopg2.connect(**self.db_config)
                self.cur = self.conn.cursor()
                print("✅ Connected to PostgreSQL!")
                return
            except Exception as e:
                print(f"⏳ Attempt {i+1}: Waiting for DB... ({e})")
                time.sleep(self.delay)
        raise ConnectionError("❌ Could not connect after retries.")

    def create_tables(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS CelebDetails (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                profession TEXT,
                birthdate DATE,
                bio TEXT
            );
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS "user" (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("✅ Tables created.")

    def insert_sample_data(self):
        self.cur.execute("""
            INSERT INTO CelebDetails (name, profession, birthdate, bio)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, ("Robert Downey Jr.", "Actor", "1965-04-04", "Plays Iron Man in Marvel movies."))

        self.cur.execute("""
            INSERT INTO "user" (username, email, password)
            VALUES (%s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, ("admin", "admin@example.com", "admin123"))

        print("✅ Sample data inserted.")
        self.conn.commit()

    def fetch_data(self):
        print("\n🎬 CelebDetails Table:")
        self.cur.execute("SELECT id, name, profession, birthdate, bio FROM CelebDetails;")
        for row in self.cur.fetchall():
            print(f"  ID: {row[0]}, Name: {row[1]}, Profession: {row[2]}, Birthdate: {row[3]}, Bio: {row[4]}")

        print("\n👤 User Table:")
        self.cur.execute('SELECT id, username, email, created_at FROM "user";')
        for row in self.cur.fetchall():
            print(f"  ID: {row[0]}, Username: {row[1]}, Email: {row[2]}, Created At: {row[3]}")

    def close(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("🔒 Connection closed.")


if __name__ == "__main__":
    DB_CONFIG = {
        "dbname": "celebdb",
        "user": "celebuser",
        "password": "celebpass",
        "host": "db",
        "port": "5432"
    }

    manager = PostgresManager(DB_CONFIG)
    try:
        manager.connect()
        manager.create_tables()
        manager.insert_sample_data()
        manager.fetch_data()
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        manager.close()
