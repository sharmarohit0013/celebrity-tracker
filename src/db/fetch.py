class DataFetcher:
    def __init__(self, cursor):
        self.cursor = cursor

    def fetch_celebs(self):
        self.cursor.execute("SELECT * FROM CelebDetails;")
        return self.cursor.fetchall()

    def individual_celeb(self, partial_name):
        self.cursor.execute("""
            SELECT * 
            FROM CelebDetails
            WHERE name ILIKE %s;
        """, (f"%{partial_name}%",))
        return self.cursor.fetchall()  