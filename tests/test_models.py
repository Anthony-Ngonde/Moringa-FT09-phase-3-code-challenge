import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "John Doe")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

    def test_article_creation(self):
        author = Author(1, "John Doe")
        magazine = Magazine(1, "Tech Weekly", "Technology")
        article = Article(1, "AI in 2024", "Content about AI", author.id, magazine.id)
        self.assertEqual(article.id, 1)
        self.assertEqual(article.title, "AI in 2024")
        self.assertEqual(article.content, "Content about AI")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)

if __name__ == "__main__":
    unittest.main()