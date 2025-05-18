class TableManager:
    def __init__(self, cursor):
        self.cursor = cursor

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS CelebDetails (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            profession TEXT,
            birthdate DATE,
            bio TEXT,
            UNIQUE(name, profession, birthdate)  -- Assuming name + birthdate uniquely identifies a celeb
            );

        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "user" (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
