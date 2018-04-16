import unittest
from longdecimals import LongDecimal


class TestLongDecimal(unittest.TestCase):
    """Test LongDecimal class properties."""

    def test_repr_method(self):
        """Test __repr__ method."""
        ciphers = [1, 2, 3]
        ld = LongDecimal(ciphers=ciphers)
        expected_result = '1.23'
        self.assertEqual(ld.__repr__, expected_result)


if __name__ == '__main__':
    unittest.main()
