class DataDeleter:
    def __init__(self, cur):
        self.cur = cur

    def delete_celeb_by_id(self, celeb_id):
        self.cur.execute("""
            DELETE FROM CelebDetails
            WHERE id = %s;
        """, (celeb_id,))
        print(f"🗑️ Deleted Celeb with ID {celeb_id}.")

