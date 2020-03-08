import hangman
from unittest import TestCase

class TestWordGuessedCorrect(TestCase):

    def test_isWordGuessed(self):
        """
        This test case function checks if the user has guessed the
        word correctly
        """
        actual = hangman.isWordGuessed("boss", "boss")
        self.assertTrue(actual, "The word you guessed it correct")

    def test_isWordGuessed2(self):
        """
        This test case fucntion checks if the user has guessed thw word wrong
        """
        actual = hangman.isWordGuessed("boss", "boot")
        self.assertFalse(actual, "The word you guessed is not correct")
