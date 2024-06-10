# tests/test_models.py

import unittest
from models.author import Author
from models.magazine import Magazine
from models.article import Article

class TestAuthor(unittest.TestCase):

    def test_constructor_valid(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "John Doe")
    
    def test_constructor_no_id(self):
        author = Author(None, "Jane Smith")
        self.assertIsNone(author.id)
        self.assertEqual(author.name, "Jane Smith")
    
    def test_constructor_invalid_id(self):
        with self.assertRaises(ValueError):
            Author("invalid_id", "John Smith")
    
    def test_constructor_empty_name(self):
        with self.assertRaises(ValueError):
            Author(1, "")
    
    def test_constructor_invalid_name(self):
        with self.assertRaises(ValueError):
            Author(1, 12345)
    
    def test_str_representation(self):
        author = Author(1, "John Smith")
        self.assertEqual(str(author), "<1. John Smith>")

class TestMagazine(unittest.TestCase):

    def test_constructor_valid(self):
        magazine = Magazine(1, "Tech Monthly", "Technology")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Monthly")
        self.assertEqual(magazine.category, "Technology")


    
    def test_constructor_no_id(self):
        magazine = Magazine(None, "Nature Weekly", "Science")
        self.assertIsNone(magazine.id)
        self.assertEqual(magazine.name, "Nature Weekly")
        self.assertEqual(magazine.category, "Science")
    
    def test_constructor_invalid_id(self):
        with self.assertRaises(ValueError):
            Magazine("invalid_id", "Tech Monthly", "Technology")
    
    def test_constructor_empty_name(self):
        with self.assertRaises(ValueError):
            Magazine(1, "", "Technology")
    
    def test_constructor_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Magazine(1, 12345, "Technology")
    
    def test_constructor_name_too_short(self):
        with self.assertRaises(ValueError):
            Magazine(1, "A", "Technology")
    
    def test_constructor_name_too_long(self):
        with self.assertRaises(ValueError):
            Magazine(1, "ThisNameIsWayTooLongForValidation", "Technology")
    
    def test_constructor_empty_category(self):
        with self.assertRaises(ValueError):
            Magazine(1, "Tech Monthly", "")
    
    def test_constructor_invalid_category_type(self):
        with self.assertRaises(ValueError):
            Magazine(1, "Tech Monthly", 12345)
    
    def test_str_representation(self):
        magazine = Magazine(1, "Tech Monthly", "Technology")
        self.assertEqual(str(magazine), "<1. Tech Monthly, Technology>")

class TestArticle(unittest.TestCase):

    def test_constructor_valid(self):
        article = Article("Tech Trends", "Content about tech trends.", 1, 2)
        self.assertIsNone(article.id)
        self.assertEqual(article.title, "Tech Trends")
        self.assertEqual(article.content, "Content about tech trends.")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 2)
        self.assertIsNone(article.magazine_name)
    

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        self.assertEqual(article.title, "Test Title")


    def test_constructor_valid(self):
        article = Article(None, "Tech Trends", "Content about tech trends.", 1, 2)
    

if __name__ == '__main__':
    unittest.main()
