#!environment/bin/python3
from longdecimals import LongDecimal
from math import factorial


class LongDecimalEuler(LongDecimal):
    """
    Long Decimal with a constructor modified
    to obtain the i-th term of the Euler series up to a certain precision.
    """

    def __init__(self, term=None, nodecimals=1):
        """Define constructor method."""
        LongDecimal.__init__(self)
        numerator, denominator = self.euler_term(term)

        # Call as_quotient over itself using numerator, denominator, nodecimals

    def euler_term(self, i):
        """
        Obtain numerator and denominator
        of the i-th term in the Euler series.
        """
        f = factorial(i)
        numerator = (f * f) * pow(2, i+1)
        denominator = factorial(2 * i + 1)
        return numerator, denominator
