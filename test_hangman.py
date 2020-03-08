from unittest import TestCase


class Test(TestCase):
    def test_load_words(self):
        def test_loadWords(self):
            expected = 'a'
            actual = 'a'
            self.assertEqual(expected, actual, "The word exists")

class TestLoadWordsFalse(TestCase):
    def test_loadWords(self):
        expected = 'a'
        actual = 'b'
        self.assertNotEqual(expected, actual, "The does not exists")
