from database.connection import CURSOR, CONN

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.save()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        sql = 'SELECT name FROM authors WHERE id = ?'
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchone()[0]

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            sql = 'UPDATE authors SET name = ? WHERE id = ?'
            CURSOR.execute(sql, (value, self._id))
            CONN.commit()
        else:
            raise ValueError("Name must be a non-empty string")

    def save(self):
        sql = 'INSERT INTO authors (id, name) VALUES (?, ?)'
        CURSOR.execute(sql, (self._id, self._name))
        CONN.commit()