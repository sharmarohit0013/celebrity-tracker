class DataUpdater:
    def __init__(self, cursor):
        self.cursor = cursor

    def update_celeb_bio(self, celeb_id, new_bio):
        query = """
        UPDATE CelebDetails
        SET bio = %s
        WHERE id = %s;
        """
        self.cursor.execute(query, (new_bio, celeb_id))
