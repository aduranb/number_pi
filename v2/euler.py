#!environment/bin/python3
from longdecimals import LongDecimal
from math import factorial


class LongDecimalEuler(LongDecimal):
    """
    Long Decimal with a constructor modified
    to obtain the i-th term of the Euler series up to a certain precision.
    """

    def __init__(self, term=0, nodecimals=1):
        """Define constructor method."""
        if not isinstance(term, int) or not isinstance(nodecimals, int):
            raise Exception('All inputs must be integers.')
        if term < 0:
                raise Exception('Parameter term must be positive.')
        if nodecimals < 0:
                raise Exception('Parameter nodecimals must be positive.')
        self._term = term
        self._nodecimals = nodecimals
        numerator, denominator = self.euler_term(term)
        LongDecimal.__init__(self)
        self.as_quotient(
                numerator=numerator,
                denominator=denominator,
                nodecimals=nodecimals)

    def factorial_from_to(self, start, end):
            """A way to simplificate the Euler equation."""
            factor = 1
            for i in range(end + 1, start + 1):
                    factor *= i
            return factor

    def euler_term(self, i):
        """
        Obtain numerator and denominator
        of the i-th term in the Euler series.
        """
        numerator = factorial(i) * pow(2, i + 1)
        denominator = self.factorial_from_to(2 * i + 1, i)
        return numerator, denominator
