from .connection import CURSOR, CONN

def create_tables():
    CURSOR.execute('''
    CREATE TABLE authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')

    CURSOR.execute('''
    CREATE TABLE magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    )
    ''')

    CURSOR.execute('''
    CREATE TABLE articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        FOREIGN KEY(author_id) REFERENCES authors(id),
        FOREIGN KEY(magazine_id) REFERENCES magazines(id)
    )
    ''')

    CONN.commit()

def drop_tables():
    CURSOR.execute('DROP TABLE IF EXISTS articles')
    CURSOR.execute('DROP TABLE IF EXISTS authors')
    CURSOR.execute('DROP TABLE IF EXISTS magazines')
    CONN.commit()