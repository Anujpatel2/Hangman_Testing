import unittest
from unittest import TestCase
import hangman

class MyTestCase(unittest.TestCase):

    def test_getAvailableLetters(self):
        actual = hangman.getAvailableLetters("abcd")
        self.assertTrue(actual, "these are the letter that are not guessed")

    #Checks if there is atleast one word retrived from the file
    def test_loadWords(self):
        s = hangman.loadWords()
        self.assertTrue(len(s) > 0, "The file was loaded into a list of words")

    #Checks if the first word is 'a'
    def test_loadWords2(self):
        s = hangman.loadWords()
        expected="a"
        actual=s[0]
        self.assertEqual(expected,actual,"First word is the same")

    #Checks if all 55909 words were retrieved from the file
    def test_loadWords3(self):
        s=hangman.loadWords()
        expected=55909
        actual=len(s)
        self.assertEqual(expected,actual,"All the words were imported")

    def test_isWordGuessed(self):
        actual = hangman.isWordGuessed("boss", ['b','o','s'])
        self.assertTrue(actual, "The word you guessed it correct")

    def test_isWordGuessed2(self):
        actual = hangman.isWordGuessed("boss", ['b','o','t'])
        self.assertFalse(actual, "The word you guessed is not correct")


if __name__ == '__main__':
    unittest.main()

