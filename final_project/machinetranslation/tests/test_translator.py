import unittest
from translator import translateToFrench, translateToEnglish

class TestMyTranslator(unittest.TestCase):

    def test_translateToEnglish(self):
        self.assertEqual(translateToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(translateToEnglish("Bonjour"), "Street")

    def test_translateToFrench(self):
        self.assertEqual(translateToFrench("Hello"), "Bonjour")
        self.assertNotEqual(translateToFrench("Street"), "Bonjour")

unittest.main()