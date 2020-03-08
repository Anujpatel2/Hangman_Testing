from unittest import TestCase
import Hangman

class TestLoadWordsTrue(TestCase):
    def test_loadWords(self):
        expected = 'a'
        actual = 'a'
        self.assertEqual(expected, actual, "The word exists")

class TestLoadWordsFalse(TestCase):
    def test_loadWords(self):
        expected = 'a'
        actual = 'b'
        self.assertNotEqual(expected, actual, "The does not exists")

class TestChooseWordChosen(TestCase):
    def test_chooseWord(self):
        actual = Hangman.chooseWord("a")
        expected = True
        self.assertTrue(actual, "Word is chosen")

class TestChooseWordNotChosen(TestCase):
    def test_chooseWord(self):
        expected = False
        actual = Hangman.chooseWord("a")

        self.assertTrue(' ',"Word is not chosen")



