import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_author_delete(self):
        author = Author(1, "John Doe")
        author.delete()
        self.assertIsNone(author.id)

    def test_magazine_update(self):
        magazine = Magazine(1, "Tech Weekly")
        magazine.name = "Tech Monthly"
        self.assertEqual(magazine.name, "Tech Monthly")

    def test_article_update(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        article.content = "Updated Test Content"
        self.assertEqual(article.content, "Updated Test Content")

if __name__ == "__main__":
    unittest.main()
