from database.connection import CURSOR, CONN

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.save()

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        sql = 'SELECT name FROM magazines WHERE id = ?'
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchone()[0]

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            sql = 'UPDATE magazines SET name = ? WHERE id = ?'
            CURSOR.execute(sql, (value, self._id))
            CONN.commit()
        else:
            raise ValueError("Name must be a string between 2 and 16 characters inclusive")

    @property
    def category(self):
        sql = 'SELECT category FROM magazines WHERE id = ?'
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchone()[0]

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            sql = 'UPDATE magazines SET category = ? WHERE id = ?'
            CURSOR.execute(sql, (value, self._id))
            CONN.commit()
        else:
            raise ValueError("Category must be a non-empty string")

    def save(self):
        sql = 'INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)'
        CURSOR.execute(sql, (self._id, self._name, self._category))
        CONN.commit()

    def articles(self):
        sql = '''
        SELECT a.id, a.title
        FROM articles a
        JOIN magazines m ON a.magazine_id = m.id
        WHERE m.id = ?
        '''
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchall()

    def contributors(self):
        sql = '''
        SELECT DISTINCT au.id, au.name
        FROM authors au
        JOIN articles a ON a.author_id = au.id
        JOIN magazines m ON a.magazine_id = m.id
        WHERE m.id = ?
        '''
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchall()

    def article_titles(self):
        sql = '''
        SELECT a.title
        FROM articles a
        JOIN magazines m ON a.magazine_id = m.id
        WHERE m.id = ?
        '''
        CURSOR.execute(sql, (self._id,))
        return [row[0] for row in CURSOR.fetchall()]

    def contributing_authors(self):
        sql = '''
        SELECT au.id, au.name
        FROM authors au
        JOIN articles a ON a.author_id = au.id
        JOIN magazines m ON a.magazine_id = m.id
        WHERE m.id = ?
        GROUP BY au.id, au.name
        HAVING COUNT(a.id) > 2
        '''
        CURSOR.execute(sql, (self._id,))
        return CURSOR.fetchall()
