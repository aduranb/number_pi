import unittest
# from longdecimals import LongDecimal
from computepi import LongDecimalEuler
from math import factorial


class TestComputePi(unittest.TestCase):
    """Test the computation of Pi."""

    def test_euler_term_method(self):
        """Test euler_term(i)."""
        i = 3
        f = factorial(i)
        expected_numerator = (f * f) * pow(2, i+1)
        expected_denominator = factorial(2 * i + 1)

        lde = LongDecimalEuler()

        num, den = lde.euler_term(i)

        self.assertEqual(num, expected_numerator)
        self.assertEqual(den, expected_denominator)




if __name__ == '__main__':
    unittest.main()
