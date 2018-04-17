#!environment/bin/python3


class LongDecimal():
    """A number with a long list of decimals."""

    def __init__(self, ciphers=[0], negative=False):
        """Define constructor method."""
        if not isinstance(ciphers, list):
            raise Exception('The parameter ciphers must be a list.')
        if any([not isinstance(cipher, int) for cipher in ciphers]):
            raise Exception('Some of the items in "ciphers" are not integers.')
        if not isinstance(negative, bool):
            raise Exception('The parameter negative must be a boolean.')

        if any([cipher < 0 for cipher in ciphers]):
            self._negative = True
        else:
            self._negative = negative

        self._ciphers = [abs(cipher) for cipher in ciphers]

    def nodecimals(self):
        """Return number of decimals."""
        return len(self._ciphers) - 1

    def iszero(self):
        """Return True if all ciphers are zero."""
        return all(cipher == 0 for cipher in self._ciphers)

    def isnegative(self):
        """Return True if negative."""
        return self._negative

    def carryover(self):
        """Ammends the ciphers to ensure all of them fall in [0,10]."""
        for i in range(1, self.nodecimals + 1):
            tens = self._ciphers[i] // 10
            if tens > 0:
                self._ciphers[i] -= 10 * tens
                self._ciphers[i - 1] += 10

    def __repr__(self):
        """Print LongDecimal instance."""
        nodecimals = self.nodecimals()
        if self._negative:
            return "-", str(self._ciphers[0]) + "." + ''.join(
                [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])
        return str(self._ciphers[0]) + "." + ''.join(
                [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])
