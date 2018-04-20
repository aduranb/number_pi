import unittest
# from longdecimals import LongDecimal
from euler import LongDecimalEuler
from math import factorial


class TestComputePi(unittest.TestCase):
    """Test the computation of Pi."""

    def test_euler_term_method(self):
        """Test euler_term(i)."""
        i = 3
        f = factorial(i)
        expected_numerator = (f * f) * pow(2, i+1)
        expected_denominator = factorial(2 * i + 1)

        lde = LongDecimalEuler(i)

        num, den = lde.euler_term(i)

        self.assertEqual(num, expected_numerator)
        self.assertEqual(den, expected_denominator)

    def test_LongDecimalEuler_construction(self):
            """Test that the instantiation works as expected."""
            i = 3
            # f = factorial(i)
            # expected_numerator = (f * f) * pow(2, i+1)
            # expected_denominator = factorial(2 * i + 1)
            expected_ciphers = [0, 1, 1, 4, 2, 8, 5, 7]
            lde = LongDecimalEuler(term=i, nodecimals=7)

            self.assertTrue(isinstance(lde._ciphers, list))
            self.assertTrue(isinstance(lde._negative, bool))
            self.assertEqual(lde._ciphers, expected_ciphers)


if __name__ == '__main__':
    unittest.main()
