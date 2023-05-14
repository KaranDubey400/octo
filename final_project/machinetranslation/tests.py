import unittest
from translator import english_to_french, french_to_english
import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)


class TestTranslation(unittest.TestCase):

    def test_english_to_french(self):
        # Test for null input
        self.assertEqual(english_to_french(None), "")

        # Test for the translation of the word 'Hello'
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english(self):
        # Test for null input
        self.assertEqual(french_to_english(None), "")

        # Test for the translation of the word 'Bonjour'
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()
