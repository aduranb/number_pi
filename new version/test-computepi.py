#!environment/bin/python3
import unittest
from computepi import compute_pi


class TestComputePi(unittest.TestCase):
    """Test number pi computation."""

    def test_compute_pi_without_decimals(self):
        """Compute pi must return 3 if nodecimals isn't input."""
        pi = compute_pi()

        self.assertEqual(pi._ciphers, [3])
        self.assertFalse(pi._negative)

    def test_nodecimals_is_positive_int(self):
        """The parameter nodecimals must be a positive integer."""
        with self.assertRaises(Exception):
                compute_pi(-1)
        with self.assertRaises(Exception):
                compute_pi("aaa")

    def test_fast_compute_pi(self):
        """Test a small number of decimals of pi."""

        pi = compute_pi(4)

        expected_result = [3, 1, 4, 1, 5]

        self.assertEqual(pi._ciphers, expected_result)



if __name__ == '__main__':
    unittest.main()
