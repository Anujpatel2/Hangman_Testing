from unittest import TestCase

import hangman


class Test(TestCase):
    def test_load_words(self):
        s= hangman.loadWords()
        self.assertTrue(len(s)>0)

    def test_loadWords(self):
        expected = 'a'
        actual = 'b'
        self.assertNotEqual(expected, actual, "The does not exists")
