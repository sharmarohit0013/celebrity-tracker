class DataInserter:
    def __init__(self, cursor):
        self.cursor = cursor

    def insert_sample_data(self):
        self.cursor.execute("""
            INSERT INTO CelebDetails (name, profession, birthdate, bio)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, ("Robert Downey Jr.", "Actor", "1965-04-04", "Plays Iron Man in Marvel movies."))
