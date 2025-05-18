class DataInserter:
    def __init__(self, cursor):
        self.cursor = cursor  # saved as self.cursor

    def insert_celeb(self, name, profession, birthdate, bio):
        self.cursor.execute("""
            SELECT COUNT(*) FROM CelebDetails
            WHERE name = %s AND profession = %s AND birthdate = %s;
        """, (name, profession, birthdate))
        
        if self.cursor.fetchone()[0] == 0:
            self.cursor.execute("""
                INSERT INTO CelebDetails (name, profession, birthdate, bio)
                VALUES (%s, %s, %s, %s);
            """, (name, profession, birthdate, bio))
            print(f"✅ Inserted celeb: {name}")
        else:
            print(f"ℹ️ Celeb already exists: {name}")
