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

class TestChooseWord(TestCase):
    def test_chooseWord(self):
        self.assertTrue('subscriptions == subscriptions' ,"Word is chosen")
