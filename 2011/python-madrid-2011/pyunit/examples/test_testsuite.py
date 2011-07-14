import unittest

class TestTestSuite(unittest.TestCase):
    def setUp(self):
        print "Running setUp1"

    def test_trivial1(self):
        self.assertTrue(True)

    def test_trivial2(self):
        self.assertTrue(True)

class TestTestSuite2(unittest.TestCase):
    def setUp(self):
        print "Running setUp2"

    def test_trivial1(self):
        self.assertTrue(True)

    def test_trivial2(self):
        self.assertTrue(True)

class TestTestSuite3(unittest.TestCase):
    def setUp(self):
        print "Running setUp3"

    def test_trivial1(self):
        self.assertTrue(True)

    def test_trivial2(self):
        self.assertTrue(True)

testsuite = unittest.TestSuite()
testsuite.addTest(TestTestSuite("test_trivial1"))
testsuite.addTest(TestTestSuite("test_trivial2"))
testsuite.addTest(TestTestSuite3("test_trivial1"))
testsuite.addTest(TestTestSuite3("test_trivial2"))

#if __name__=='__main__':
#    unittest.main()
