# Project Architecture
>This documentation is linked to v2.0

As stated in the [Python documentation](https://docs.python.org/3.6/tutorial/floatingpoint.html):
>On most machines today, floats are approximated using a binary fraction with the numerator using the first 53 bits starting with the most significant bit and with the denominator as a power of two.

Note that this is in the very nature of binary floating-point. The compiler, intelligently, keeps the number of digits manageable by displaying a rounded value instead.
If we want to see what the math library can provide, we may wish to use string formatting:
```
>>> repr(math.pi)
'3.141592653589793'
```
Although this are probably more decimals than pretty much any use case of pi needs, for our purposes, this isn't enough.

## LongDecimal

Thus, we need to create a Data structure called LongDecimal with the following features:

1. It contains a list of integers, called ciphers, constrained to be between 0 and 9 (both inclusive), and a boolean that defines whether the number is positive or negative.
2. I can sum two decimals using the + sign.
3. I can tell whether the LongDecimal is zero or not up to a number of decimals.
4. I can rearrange the precision at will; that is, I can set the number of decimals of a LongDecimal after instantiation.
5. I can apply abs() to the LongDecimal.
6. I can draw comparisons between LongDecimals (>, >=, <, <=, ==).

Let's have a look at each of these features one by one with references to the class stored in `longdecimals.py`.

#### LongDecimal contains ciphers and a sign-defining boolean

The instance variables in the class will be a list called _ciphers, and the sign will be represented by a boolean called _negative, which will be True if the object is defined below 0 and False otherwise.

The list ciphers must contain integers that fall under the [0, 9] bracket, thus we need to define a carryover() method that rearrange each cipher by means of adding or substracting from the previous decimal:

```python
def carryover(self):
      """Ammends the ciphers to ensure all of them fall in [0,10)."""
      if self._ciphers[0] < 0:
              self._negative = True
              self._ciphers[0] = abs(self._ciphers[0])

      for i in range(1, len(self._ciphers)):
          while self._ciphers[-i] >= 10:
              self._ciphers[-i] -= 10
              self._ciphers[-i - 1] += 1
          while self._ciphers[-i] < 0:
              self._ciphers[-i] += 10
              self._ciphers[-i - 1] -= 1
```

This serves three purposes:
1. For positive numbers bigger than 10, we carry over the tens to the previous decimal. This won't apply to the first cipher (the actual integer point).
2. For negative numbers, we carry back a ten from the previous decimal. This won't apply to the first cipher (the actual integer point).
3. If the integer point is negative, we set it as positive and turn self._negative as True.

Once we defined this method, we can define the `__init__` method as follows:

```python
def __init__(self, ciphers=[0], negative=False):
      """Define constructor method."""
      if not isinstance(ciphers, list):
          raise Exception('The parameter ciphers must be a list.')
      if any([not isinstance(cipher, int) for cipher in ciphers]):
          raise Exception('Some of the items in "ciphers" are not integers.')
      if not isinstance(negative, bool):
          raise Exception('The parameter negative must be a boolean.')

      self._ciphers = ciphers
      self._negative = negative
      self.carryover()
```
This raises an exception for invalid inputs, and calls carryover() immediately after instantiating the class.

#### Drawing comparison
This are the dunder methods needed to compare two LongDecimals

```python
def __eq__(self, ld):
    """Return True if self == ld."""
    if self._ciphers == ld._ciphers:
        return True
    return False
```

```python
def __gt__(self, other):
    """self > other"""
    if not isinstance(other, LongDecimal):
        raise Exception("""Module comparison not defined
                                        when other is not LongDecimal""")
    # If equal, then false
    if self._ciphers == other._ciphers:
        return False
    nodecimals = max(len(self), len(other))
    i = 0
    # One by one, if I find something different, return True or False accordingly
    while i < nodecimals:
        if self._ciphers[i] < other._ciphers[i]:
            return False
        if self._ciphers[i] > other._ciphers[i]:
            return True
        i += 1
```

#### Sum of LongDecimals
The sum of two LongDecimals can be defined based on the _negative variable of both of them:
