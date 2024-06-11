from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'<{self.id}. {self.name}>'

    def _create_author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("ID must be an integer or None")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.*
            FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines