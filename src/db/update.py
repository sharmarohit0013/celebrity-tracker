class DataUpdater:
    def __init__(self, cur):
        self.cur = cur

    def update_celeb_bio(self, celeb_id, new_bio):
        self.cur.execute("""
            UPDATE CelebDetails
            SET bio = %s
            WHERE id = %s;
        """, (new_bio, celeb_id))
        print(f"✅ Updated bio for Celeb ID {celeb_id}.")
