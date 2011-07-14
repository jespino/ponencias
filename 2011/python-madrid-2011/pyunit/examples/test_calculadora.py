#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = calculadora.Calculadora()

    def test_suma(self):
        result = self.calc.suma(1,1)
        self.assertEqual(result, 2)

        result = self.calc.suma(1,-1)
        self.assertEqual(result, 0)

        result = self.calc.suma(1,-2)
        self.assertEqual(result, -1)

    def test_resta(self):
        result = self.calc.resta(1,7)
        self.assertEqual(result, -6)

        result = self.calc.resta(1,1)
        self.assertEqual(result, 0)

        result = self.calc.resta(1,-1)
        self.assertEqual(result, 2)

        result = self.calc.resta(1,-2)
        self.assertTrue(result == 3)

    def test_multiplica(self):
        result = self.calc.multiplica(1,7)
        self.assertEqual(result, 7)

        result = self.calc.multiplica(0,7)
        self.assertEqual(result, 0)

        result = self.calc.multiplica(3,7)
        self.assertEqual(result, 21)

        result = self.calc.multiplica(1,-1)
        self.assertEqual(result, -1)

    def test_divide(self):
        result = self.calc.divide(10,2)
        self.assertEqual(result, 5)

        result = self.calc.divide(0,10)
        self.assertEqual(result, 0)

        result = self.calc.divide(10,0)
        self.assertEqual(result, "infinito")

        result = self.calc.divide(0,0)
        self.assertEqual(result, "indeterminación")

if __name__ == '__main__':
    unittest.main()
