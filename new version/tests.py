import unittest
import random
from longdecimals import LongDecimal


def ciphers_generator():
        """Generate a valid ciphers list of up to 9 decimals."""
        return [random.randint(0, 9) for i in range(random.randint(1, 10))]


class TestLongDecimal(unittest.TestCase):
    """Test LongDecimal class properties."""

    def test_iszero_method(self):
        """Test iszero method."""
        ciphers = ciphers_generator()
        ld = LongDecimal(ciphers=ciphers)
        zero = LongDecimal(ciphers=[0])
        zerodefault = LongDecimal()

        self.assertFalse(ld.iszero())
        self.assertTrue(zero.iszero())
        self.assertTrue(zerodefault.iszero())

    def test_nodecimals_method(self):
        """Test nodecimals method."""
        ciphers = ciphers_generator()
        ld = LongDecimal(ciphers=ciphers)

        expected_result = len(ciphers) - 1
        self.assertEqual(ld.nodecimals(), expected_result)

    def test_repr_method(self):
        """Test __repr__ method."""
        ciphers = [1, 2, 3]
        ld = LongDecimal(ciphers=ciphers)
        expected_result = '1.23'
        self.assertEqual(ld.__repr__(), expected_result)

    def test_isnegative(self):
        """Test isnegative method."""
        ciphers = ciphers_generator()
        ld = LongDecimal(ciphers=ciphers, negative=True)

        self.assertTrue(ld.isnegative())

    def test_negative_ciphers_negative_by_default(self):
            """
            Long Decimal must be negative by default
            if any cipher in ciphers is negative.
            """
            ciphers_1 = [-1, 2, 3]
            ciphers_2 = [1, -2, 3]
            ld1 = LongDecimal(ciphers=ciphers_1)
            ld2 = LongDecimal(ciphers=ciphers_2)

            self.assertTrue(ld1.isnegative())
            self.assertTrue(ld2.isnegative())

    def test_negative_ciphers_turn_all_positive(self):
            """Long Decimal must return all ciphers positive."""
            ciphers_1 = [-1, 2, 3]
            ciphers_2 = [1, -2, 3]
            expected_ciphers_stored = [1, 2, 3]
            ld1 = LongDecimal(ciphers=ciphers_1)
            ld2 = LongDecimal(ciphers=ciphers_2)

            self.assertEqual(ld1._ciphers, expected_ciphers_stored)
            self.assertEqual(ld2._ciphers, expected_ciphers_stored)

    def test_exception_raised_when_ciphers_not_a_list(self):
            """An Exception is raised if any cipher is not a list."""
            invalid_ciphers = 12

            with self.assertRaises(Exception):
                    LongDecimal(ciphers=invalid_ciphers)

    def test_exception_raised_when_ciphers_not_int(self):
            """An Exception is raised if any cipher is not int."""
            invalid_ciphers = [1, 2, 3.3]

            with self.assertRaises(Exception):
                    LongDecimal(ciphers=invalid_ciphers)


if __name__ == '__main__':
    unittest.main()
