from unittest import TestCase

import hangman


class Test(TestCase):

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