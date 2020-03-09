import hangman
from unittest import TestCase


class TestGetAvailableLetters(TestCase):
    def test_getAvailableLetters(self):
        actual = hangman.getAvailableLetters("abcd")
        self.assertTrue(actual, "these are the letter that are not guessed")
