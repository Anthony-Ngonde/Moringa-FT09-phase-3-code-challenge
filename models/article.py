from database.connection import CURSOR, CONN

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.save()

    def __repr__(self):
        return f'<Article {self.title}>'
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        sql = 'SELECT title FROM articles WHERE id = ?'
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchone()[0]

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            sql = 'UPDATE articles SET title = ? WHERE id = ?'
            CURSOR.execute(sql, (value, self._id))
            CONN.commit()
        else:
            raise ValueError("Title must be a string between 5 and 50 characters inclusive")

    @property
    def content(self):
        sql = 'SELECT content FROM articles WHERE id = ?'
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchone()[0]

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            sql = 'UPDATE articles SET content = ? WHERE id = ?'
            CURSOR.execute(sql, (value, self._id))
            CONN.commit()
        else:
            raise ValueError("Content must be a string")

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    def save(self):
        sql = '''
        INSERT INTO articles (id, title, content, author_id, magazine_id)
        VALUES (?, ?, ?, ?, ?)
        '''
        CURSOR.execute(sql, (self._id, self._title, self._content, self._author_id, self._magazine_id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, article_id):
        sql = 'SELECT id, title, content, author_id, magazine_id FROM articles WHERE id = ?'
        CURSOR.execute(sql, (article_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def all(cls):
        sql = 'SELECT id, title, content, author_id, magazine_id FROM articles'
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_title(cls, title):
        sql = 'SELECT id, title, content, author_id, magazine_id FROM articles WHERE title = ?'
        CURSOR.execute(sql, (title,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    @property
    def author(self):
        sql = '''
        SELECT au.id, au.name
        FROM authors au
        JOIN articles a ON a.author_id = au.id
        WHERE a.id = ?
        '''
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchone()

    @property
    def magazine(self):
        sql = '''
        SELECT m.id, m.name
        FROM magazines m
        JOIN articles a ON a.magazine_id = m.id
        WHERE a.id = ?
        '''
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchone()
