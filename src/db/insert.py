class DataInserter:
    def __init__(self, cursor):
        self.cursor = cursor

    def insert_celeb(self, name, profession, birthdate, bio):
        self.cur.execute("""
            SELECT COUNT(*) FROM CelebDetails
            WHERE name = %s AND profession = %s AND birthdate = %s;
        """, (name, profession, birthdate))
        
        if self.cur.fetchone()[0] == 0:
            self.cur.execute("""
                INSERT INTO CelebDetails (name, profession, birthdate, bio)
                VALUES (%s, %s, %s, %s);
            """, (name, profession, birthdate, bio))
            print(f"✅ Inserted celeb: {name}")
        else:
            print(f"ℹ️ Celeb already exists: {name}")
