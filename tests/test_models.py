import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine


class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(name="John Doe")
        author.save()
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(title="Test Title", content="Test Content", author_id=1, magazine_id=1)
        article.save()
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(name="Tech Weekly", category="Technology")
        magazine.save()
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_author_delete(self):
        author = Author(name="John Doe")
        author.save()
        author.delete()
        self.assertIsNone(author.id)

    def test_magazine_update(self):
        magazine = Magazine(name="Tech Weekly", category="Technology")
        magazine.save()
        magazine.name = "Tech Monthly"
        magazine.save()
        self.assertEqual(magazine.name, "Tech Monthly")

    def test_article_update(self):
        article = Article(title="Test Title", content="Test Content", author_id=1, magazine_id=1)
        article.save()
        article.content = "Updated Test Content"
        article.save()
        self.assertEqual(article.content, "Updated Test Content")

if __name__ == "__main__":
    unittest.main()
