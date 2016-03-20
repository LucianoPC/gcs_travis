#!/usr/bin/env python

import unittest

from src.math_operations import MathOperations

class PkgClassificationTests(unittest.TestCase):

    def test_sum(self):
        math_operations = MathOperations()
        number_one, number_two = 10, 5
        result = 15

        self.assertEqual(result, math_operations.sum(number_one, number_two))
