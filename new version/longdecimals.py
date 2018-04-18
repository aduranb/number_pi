#!environment/bin/python3


class LongDecimal():
    """
    A number with a long list of decimals.

    Comparison (>,<, >=, <=, ==) is done at the modular level.
    That means, it only compares the modules,
    regardless of the instances being positive or negative.

    LongDecimal(ciphers=[7,8,9], negative= True) == LongDecimal(ciphers=[7,8,9], negative= False)
    returns True

    LongDecimal(ciphers=[2,0,0], negative= True) > LongDecimal(ciphers=[1,0,0], negative= False)
    returns True
    """

    def __init__(self, ciphers=[0], negative=False):
        """Define constructor method."""
        if not isinstance(ciphers, list):
            raise Exception('The parameter ciphers must be a list.')
        if any([not isinstance(cipher, int) for cipher in ciphers]):
            raise Exception('Some of the items in "ciphers" are not integers.')
        if not isinstance(negative, bool):
            raise Exception('The parameter negative must be a boolean.')

        self._ciphers = ciphers
        self.carryover()

        if any([cipher < 0 for cipher in ciphers]):
            self._negative = True
            self._ciphers = [abs(cipher) for cipher in ciphers]
        else:
            self._negative = negative

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
        """Ammends the ciphers to ensure all of them fall in [0,10)."""
        for i in range(1, len(self._ciphers)):
            while self._ciphers[-i] >= 10:
                self._ciphers[-i] -= 10
                self._ciphers[-i - 1] += 1
            while self._ciphers[-i] < 0:
                self._ciphers[-i] += 10
                self._ciphers[-i - 1] -= 1

    def setnodecimals(self, nodecimals):
        """Set decimal precision in advance to accelerate pi computation."""
        if nodecimals > self.nodecimals:
            self.ciphers = self.ciphers + [0] * (nodecimals - self.nodecimals)
            self.nodecimals = nodecimals
        else:
            self.ciphers = self.ciphers[:nodecimals + 1:]
            self.nodecimals = nodecimals
        return self

    def dividebyten(self, keeplast=False):
        """
        Divide by ten by inserting a 0 at the beginning of ciphers.
        If not keeplast, then remove the last cipher.
        """
        self._ciphers.insert(0, 0)
        if not keeplast:
            self._ciphers.pop()
        return self

    def __repr__(self):
        """Print LongDecimal instance."""
        nodecimals = self.nodecimals()
        if self._negative:
            return "-", str(self._ciphers[0]) + "." + ''.join(
                [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])
        return str(self._ciphers[0]) + "." + ''.join(
                [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])

    def __abs__(self):
        """abs(LongDecimal)."""
        return LongDecimal(ciphers=self._ciphers, negative=False)

    def __ge__(self, other):
        """self > other"""
        if not isinstance(other, LongDecimal):
            raise Exception("""Module comparison not defined
                                            when other is not LongDecimal""")
        nodecimals = max(len(self), len(other))
        i = 0
        while i < nodecimals:
            if self._ciphers[i] < other._ciphers[i]:
                return False
            i += 1
        return True

    def __len__(self):
        """len(LongDecimal)."""
        return len(self._ciphers)

    def __eq__(self, ld):
        """Return True if self == ld."""
        if self._ciphers == ld._ciphers:
            return True
        return False

    def __add__(self, ld):
        """self + ld operator."""

    def __radd__(self, ld):
        """ld + self operator."""
