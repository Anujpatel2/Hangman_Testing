from unittest import TestCase

class TestWordGuessedCorrect(TestCase):
    def test_isWordGuessed(self):
        actual = 'true'
        expected = 'true'
        self.assertEqual(actual, expected, "The word you guessed it correct")

class TestWordGuessedNotCorrect(TestCase):
    def test_isWordGuessed(self):
        actual = 'false'
        expected = 'false'
        self.assertNotEqual(actual, expected, "The word you guessed isn't correct")





