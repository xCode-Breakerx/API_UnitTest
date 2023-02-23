import sqlite3
from sqlite3 import Connection, Cursor


class db_test():
    conn: Connection

    def __init__(self) -> None:
        self.conn: Connection = sqlite3.connect(':memory:', check_same_thread=False)
        self.init_db()

    def init_db(self):
        try:
            cur: Cursor = self.conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS user (id integer PRIMARY KEY,name text NOT NULL, age int NOT NULL);")
            if not len(self.fetchall()):
                cur.execute("INSERT INTO user(name,age) VALUES('ligma',69)")
            self.conn.commit()
        except:
            self.conn.rollback()
            raise

    def insert(self, name, age):
        try:
            cur: Cursor = self.conn.cursor()
            cur.execute("INSERT INTO user(name,age) VALUES(?,?)", (name, age))
            self.conn.commit()
        except:
            self.conn.rollback()
            raise

    def delete(self, name):
        try:
            cur: Cursor = self.conn.cursor()
            cur.execute("DELETE FROM user WHERE user.name=?", (name,))
            self.conn.commit()
        except:
            self.conn.rollback()
            raise

    def update(self, user_id, new_name, new_age):
        try:
            cur: Cursor = self.conn.cursor()
            cur.execute("SELECT * FROM user WHERE user.id=?", (user_id,))
            if cur.fetchone() is not None:
                cur.execute("UPDATE user SET name=?, age=? WHERE user.id=?", (new_name, new_age, user_id))
                self.conn.commit()
                return True

            return False
        except:
            self.conn.rollback()
            raise

    def fetch(self, name):
        try:
            cur: Cursor = self.conn.cursor()
            cur.execute("SELECT * from user WHERE user.name=?", (name,))
            fetchone = cur.fetchone()
            if fetchone is not None:
                return dict(zip((col[0] for col in cur.description), (x for x in fetchone)))
            else:
                return {}
        except:
            raise

    def fetchall(self):
        try:
            cur: Cursor = self.conn.cursor()
            cur.execute("SELECT * from user")
            return [dict(zip((column[0] for column in cur.description), x)) for x in cur.fetchall()]
        except:
            raise
