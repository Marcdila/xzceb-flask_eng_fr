import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        TESTS = [
            ("Hello", "Bonjour"),
            ("Red", "Rouge"),
            ("Gold", "Or"),
            ("", "")
        ]

        for original, translated in TESTS:
            self.assertEqual(english_to_french(original), translated)

class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        TESTS = [
            ("Bonjour", "Hello"),
            ("Bleu", "Blue"),
            ("Jaune", "Yellow"),
            ("", "")
        ]

        for original, translated in TESTS:
            self.assertEqual(french_to_english(original), translated)

unittest.main()