#!environment/bin/python3


class LongDecimal():
    """A number with a long list of decimals."""

    def __init__(self, ciphers=[0], negative=False):
        """Define constructor method."""
        self._negative = negative
        self._ciphers = ciphers

    def nodecimals(self):
        """Return number of decimals."""
        return len(self._ciphers) - 1

    def iszero(self):
        """Return True if all ciphers are zero."""
        return all(cipher == 0 for cipher in self._ciphers)

    def __repr__(self):
        """Print LongDecimal instance."""
        nodecimals = self.nodecimals()
        if self._negative:
            return "-", str(self._ciphers[0]) + "." + ''.join(
                [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])
        return str(self._ciphers[0]) + "." + ''.join(
                [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])
