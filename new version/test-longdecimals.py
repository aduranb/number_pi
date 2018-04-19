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
            self.assertFalse(ld2.isnegative())

    def test_negative_ciphers_turn_all_positive(self):
            """Long Decimal must return all ciphers positive."""
            ciphers_1 = [-1, 2, 3]
            expected_ciphers_stored = [1, 2, 3]
            ld1 = LongDecimal(ciphers=ciphers_1)

            self.assertEqual(ld1._ciphers, expected_ciphers_stored)

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

    def test_carry_over(self):
            """All ciphers must fall within [0, 10)."""
            ciphers = [0, 12, 30, 1]
            expected_result = [1, 5, 0, 1]

            ld = LongDecimal(ciphers=ciphers)
            self.assertEqual(ld._ciphers, expected_result)

    def test_a_negative_cipher_is_carried_over(self):
            """
            Test that negative ciphers are carried over:
            When substracting two numbers, negative ciphers may appear.
            If that happens, the previous cipher must be reduced by the
            adequate amount to make that negative cipher back to [0, 10).
            """
            ciphers = [1, -2, 3]
            expected_result = [0, 8, 3]
            ld = LongDecimal(ciphers=ciphers)

            self.assertEqual(ld._ciphers, expected_result)

    def test_dividebyten_method(self):
            """
            Test that divide by ten method works as expected:
            insert a 0 at the beginning of the ciphers list.
            keeplast=False, then len(ciphers)
            remains constant after applying method;
            keeplast=True, then len(ciphers_after) = len(ciphers_before) + 1.
            """
            ciphers = ciphers_generator()
            ld = LongDecimal(ciphers=ciphers)

            len_before = len(ciphers)
            self.assertEqual(len_before, len(ld._ciphers))

            ld.dividebyten(keeplast=True)

            # Length increments by 1
            self.assertEqual(len_before + 1, len(ld._ciphers))

            ld.dividebyten(keeplast=False)

            # Now length remains constant
            self.assertEqual(len_before + 1, len(ld._ciphers))

            # And new ciphers is the same ciphers with a 0 upfront
            ciphers.insert(0, 0)
            self.assertEqual(ld._ciphers, ciphers)

    def test_setprecision_with_less_precision(self):
            """
            Test setprecision method
            when new_precision < current_precision.
            """
            ciphers = [1, 2, 3, 4, 5]
            ld = LongDecimal(ciphers=ciphers)

            self.assertEqual(len(ld), len(ciphers))
            new_precision = 2

            ld.setprecision(new_precision=new_precision)

            self.assertEqual(len(ld), new_precision + 1)
            self.assertEqual(ld._ciphers, ciphers[:new_precision + 1])

    def test_setprecision_with_more_precision(self):
            """
            Test setprecision method
            when new_precision > current_precision.
            """
            ciphers = [1, 2, 3, 4, 5]
            ld = LongDecimal(ciphers=ciphers)

            new_precision = 5

            ld.setprecision(new_precision=new_precision)

            self.assertEqual(len(ld), new_precision + 1)
            self.assertEqual(ld._ciphers, ciphers + [0] * (
                new_precision - len(ciphers) + 1))

    def test_setprecision_with_same_precision(self):
            """
            Test that setprecision with the same precision
            doesn't change the Long Decimal.
            """
            ciphers = [1, 2, 3, 4, 5]
            ld = LongDecimal(ciphers=ciphers)

            new_precision = len(ciphers) - 1

            ld.setprecision(new_precision=new_precision)

            self.assertEqual(len(ld), len(ciphers))
            self.assertEqual(ld._ciphers, ciphers)

    def test_as_quotient_without_nodecimals(self):
            """
            When nodecimals is not input,
            as_quotient must return the number as an integer
            in a LongDecimal format.
            """
            numerator = 4
            denominator = 3

            ld = LongDecimal().as_quotient(
                        numerator=numerator, denominator=denominator)
            self.assertEqual([1], ld._ciphers)


    def test_magic_method_abs(self):
            """Test __abs__ method."""
            ciphers = ciphers_generator()
            ld1 = LongDecimal(ciphers=ciphers)
            ld2 = LongDecimal(ciphers=ciphers, negative=True)

            abs_1 = abs(ld1)
            abs_2 = abs(ld2)

            self.assertEqual(abs_1._ciphers, ciphers)
            self.assertFalse(abs_1._negative)

            self.assertEqual(abs_2._ciphers, ciphers)
            self.assertFalse(abs_2._negative)

    def test_magic_method_len(self):
            """Test __len__ method."""
            ciphers = ciphers_generator()
            ld = LongDecimal(ciphers=ciphers)

            self.assertEqual(len(ciphers), len(ld))

    def test_magic_method_ge(self):
            """Test __ge__ method."""
            ciphers_greater = [1, 2, 3]
            ciphers_equal = [1, 1, 3]
            ciphers_less = [1, 1, 2]

            ld_greater = LongDecimal(ciphers=ciphers_greater)
            ld_equal_1 = LongDecimal(ciphers=ciphers_equal)
            ld_equal_2 = LongDecimal(ciphers=ciphers_equal)
            ld_less = LongDecimal(ciphers=ciphers_less)

            self.assertTrue(ld_greater >= ld_equal_1)
            self.assertTrue(ld_equal_1 >= ld_equal_2)
            self.assertTrue(ld_equal_1 >= ld_less)
            self.assertTrue(ld_equal_2 >= ld_less)

            self.assertFalse(ld_less >= ld_equal_1)
            self.assertFalse(ld_less >= ld_equal_2)
            self.assertFalse(ld_equal_1 >= ld_greater)
            self.assertFalse(ld_equal_2 >= ld_greater)

    def test_magic_method_eq(self):
            """Test __eq__ method."""
            ciphers = ciphers_generator()
            ciphers_2 = ciphers_generator()
            ld = LongDecimal(ciphers=ciphers)
            ld2 = LongDecimal(ciphers=ciphers_2)
            ld3 = LongDecimal(ciphers=ciphers)

            self.assertFalse(ld == ld2)
            self.assertTrue(ld == ld3)
            self.assertFalse(ld is ld3)

    def test_magic_method_add(self):
            """Test __add__ method."""
            ciphers_1 = [1, 2, 3, 4]
            ld_1 = LongDecimal(ciphers=ciphers_1)
            ciphers_2 = [5, 6, 7, 8]
            ld_2 = LongDecimal(ciphers=ciphers_2)
            expected_result = [6, 9, 1, 2]
            ld_3 = ld_1 + ld_2

            self.assertEqual(ld_3._ciphers, expected_result)







if __name__ == '__main__':
    unittest.main()
