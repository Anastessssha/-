# Бессонова Анастасия 44-22-122 задание 2
import math
import sys
import unittest


def main(*args):
    try:
        x = float(args[0][1])
        if x < 0:
            return math.log10(math.sqrt(x ** 2 + 3.44))
        else:
            return math.sqrt(x ** 2 - 0.48 * x)
    except:
        return "Произошла ошибка"

class SolverOfASystemOfEquationsTestCase(unittest.TestCase):
    def test_le(self):
        res = main(['...', 0.5])
        self.assertEqual(res, 0.10000000000000005)

    def test_r(self):
        res = main(['...', 0.9])
        self.assertEqual(res, 0.6148170459575759)

    def test_error(self):
        res = main()
        self.assertEqual(res, "Произошла ошибка")