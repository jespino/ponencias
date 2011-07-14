import unittest

class TestTestSuite(unittest.TestCase):
    def test_trivial1(self):
        self.assertTrue(True)

    def test_trivial2(self):
        self.assertTrue(True)

if __name__=='__main__':
    unittest.main()
