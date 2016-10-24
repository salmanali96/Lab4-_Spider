import unittest

class unittests(object):

    def test_upper(self):
        self.assertEqual('.txt'.upper(), 'TXT')

    def test_isupper(self):
        self.assertTrue('TXT'.isupper())
        self.assertFalse('txt'.isupper())

    def test_split(self):
        s = 'Salman txt'
        self.assertEqual(s.split(), ['Salman', 'txt'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
