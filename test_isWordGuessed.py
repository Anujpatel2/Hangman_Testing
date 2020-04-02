import hangman
from unittest import TestCase

class TestWordGuessedCorrect(TestCase):

    def test_isWordGuessed(self):
        actual = hangman.isWordGuessed("boss", "boss")
        self.assertTrue(actual, "The word you guessed it correct")

    def test_isWordGuessed2(self):
        actual = hangman.isWordGuessed("boss", "boot")
        self.assertFalse(actual, "The word you guessed is not correct")