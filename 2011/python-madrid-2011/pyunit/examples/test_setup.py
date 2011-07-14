import unittest

def setUpModule():
    print "Ejecutando setUpModule"

def tearDownModule():
    print "Ejecutando tearDownModule"


class TestSetUp(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print "Ejecutando setUpClass"

    @classmethod
    def tearDownClass(self):
        print "Ejecutando tearDownClass"

    def setUp(self):
        print "Ejecutando setUp"

    def tearDown(self):
        print "Ejecutando tearDown"

    def test_trivial1(self):
        self.assertTrue(True)

    def test_trivial2(self):
        self.assertTrue(True)

class TestSetUp2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print "Ejecutando setUpClass2"

    @classmethod
    def tearDownClass(self):
        print "Ejecutando tearDownClass2"

    def setUp(self):
        print "Ejecutando setUp"

    def tearDown(self):
        print "Ejecutando tearDown"

    def test_trivial1(self):
        self.assertTrue(True)

    def test_trivial2(self):
        self.assertTrue(True)

#if __name__=='__main__':
#    unittest.main()
