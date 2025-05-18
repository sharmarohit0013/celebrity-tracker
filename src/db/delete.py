class DataDeleter:
    def __init__(self, cursor):
        self.cursor = cursor

    def delete_celeb_by_id(self, celeb_id):
        query = """
        DELETE FROM CelebDetails
        WHERE id = %s;
        """
        self.cursor.execute(query, (celeb_id,))