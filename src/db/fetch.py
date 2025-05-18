class DataFetcher:
    def __init__(self, cursor):
        self.cursor = cursor

    def fetch_celebs(self):
        self.cursor.execute("SELECT * FROM CelebDetails;")
        return self.cursor.fetchall()
