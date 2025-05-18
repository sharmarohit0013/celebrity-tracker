class DataInserter:
    def __init__(self, cursor):
        self.cursor = cursor

        def insert_sample_data(self):
        # Sample celebrity data - add or modify as needed
            sample_celebs = [
                ("Tom Hanks", "Actor", "1956-07-09", "Famous Hollywood actor."),
                ("Beyonce", "Singer", "1981-09-04", "Popular singer and performer."),
                ("Elon Musk", "Entrepreneur", "1971-06-28", "CEO of Tesla and SpaceX."),
            ]
            for name, profession, birthdate, bio in sample_celebs:
                self.insert_celebrity(name, profession, birthdate, bio)

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
