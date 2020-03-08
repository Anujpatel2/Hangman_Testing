class TestLoadWordsTrue(TestCase):
    def test_loadWords(self):
        expected = 'a'
        actual = 'a'
        self.assertEqual(expected, actual, "The word exists")

class TestLoadWordsFalse(TestCase):
    def test_loadWords(self):
        expected = 'a'
        actual = 'b'
        self.assertEqual(expected, actual, "The does not exists")
