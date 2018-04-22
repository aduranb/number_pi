# Project Architecture
>This documentation is linked to v2.0.

## Contents

1. Intro
2. LongDecimal
  1. Requirements
    1. LD contains ciphers and sign-defining boolean
    2. Drawing comparison
    3.  Sum of LongDecimals
    4. LongDecimal iszero()
    5. Set precision
    6. abs()
    7. print(LongDecimal)
  2. Special methods not included as requirements
    1. as_quotient()
3. LongDecimalEuler
4. Compute Pi

## Intro

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
7. print(LongDecimal) must return a string format of the number, encapsulating the data structure so that it resembles a normal float.

Let's have a look at each of these features one by one with references to the class stored in `longdecimals.py`.

>An exhaustive test suite for this requirements can be found [here](https://github.com/ohduran/number_pi/blob/master/2.0/test-longdecimals.py).

### Requirements
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
This are the dunder methods needed to compare two LongDecimals.

Something worth notice is that this methods are only module comparison; the sign is disregarded, and we only take ciphers as the reference.

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
The sum of two LongDecimals can be defined based on the _negative variable of both of them. We store this method as the dunder `__add__`.

1. If both signs are the same, then ciphers items must be sum for each position.

```python
if self._negative == other._negative:
        ciphers = [self._ciphers[i] + other._ciphers[i]
                   for i in range(new_precision + 1)]
        return LongDecimal(ciphers=ciphers, negative=self._negative)
```

2. If signs are different, and self is bigger than other, then we substract other from self, and we keep self._negative as the result _negative

```python
if self > other:
        ciphers = [self._ciphers[i] - other._ciphers[i]
                   for i in range(new_precision + 1)]
        return LongDecimal(ciphers=ciphers, negative=self._negative)
```

3. For any other case (signs are different, and other is bigger than self), then substract self from other, and we keep other._negative as the result _negative.

```python
else:
        ciphers = [-self._ciphers[i] + other._ciphers[i]
                   for i in range(new_precision + 1)]
        return LongDecimal(ciphers=ciphers, negative=other._negative)
```

#### LongDecimal iszero()
This will be useful when we want to set a condition for the while loop.

```python
def iszero(self):
      """Return True if all ciphers are zero."""
      return all(cipher == 0 for cipher in self._ciphers)
```
#### Set the precision of LongDecimal
```python
def setprecision(self, new_precision):
    """
    Set precision as a new number of decimals,
    regardless of the length of ciphers when instantiated.
    """
    current_precision = self.nodecimals()

    # if the new precision is bigger than current one, add zeros at the end
    if new_precision > current_precision:
        self._ciphers = self._ciphers + [0] * (
                        new_precision - current_precision)
    # otherwise, slice the ciphers up to the new precision
    else:
        self._ciphers = self._ciphers[:new_precision + 1:]
```
#### Abs()
```python
def __abs__(self):
    """abs(LongDecimal)."""
    self._negative = False
    return self
```

#### print(LongDecimal)
To print a LongDecimal like a built-in float, we defined the dunder `__repr__` method:

```python
def __repr__(self):
    """Print LongDecimal instance."""
    nodecimals = self.nodecimals() # avoid constantly calling self
    # add the minus sign if the number is negative
    if self._negative:
        return "-", str(self._ciphers[0]) + "." + ''.join(
            [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])
    return str(self._ciphers[0]) + "." + ''.join(
            [str(self._ciphers[i]) for i in range(1, nodecimals + 1)])
```
### Special methods not included as requirements
A particular set of methods have been included that will facilitate the construction of terms of the Euler series.

#### as_quotient()
To facilitate the construction of a quotient between two integers without having to define a dunder method to set the logic for division, the method as_quotient() is input two integers and will transform self to become the quotient between the numerator and the denominator, with a predefined number of decimals.

The algorithm is the one we used in primary school:

1. Starting with cipher `i = 0`, substract a number of times q the divisor to the dividend, provided that dividend never becomes negative.
2. Store q as the i-th cipher.
3. Multiply dividend by 10, move onto the next cipher `i += 1`.
4. Repeat until precision is reached.

A special case for `nodecimals=0` is included: just return the ciphers list as the pure division `//` between the numerator and denominator.

One thing we found when testing the end result was that the precision wasn't good enough; thus, we decided to use extra precision (two added decimals), and constrain the result back. This improved the result without losing to much efficiency in the algorithm.

```python
def as_quotient(self, numerator, denominator, nodecimals=0):
      """
      Divide two integers and
      return the result as LongDecimal format.
      """
      if nodecimals == 0:
          ciphers = [numerator // denominator]
          self._ciphers = ciphers
          return LongDecimal(ciphers=ciphers)
      ciphers = [0] * (nodecimals + 3)

      x = numerator
      for i in range(nodecimals + 3):
          q = 0
          while x >= denominator:
              x -= denominator
              q += 1
          ciphers[i] = q
          x *= 10
      ciphers = ciphers[:nodecimals + 1]
      self._ciphers = ciphers
      return LongDecimal(ciphers=ciphers)
```

## LongDecimalEuler
Once we've set up a float number, we wanted to create a more specific set of LongDecimal that could be instantiated directly as terms of the Euler series, such as LongDecimalEuler(term=term). The requirements were as follows:

1. LongDecimalEuler must inherit from LongDecimal to keep the features of a LongDecimal.
2. It must be instantiated not as ciphers or sign, but as terms in the Euler series defined in the Mathematical Approach.

>An exhaustive test suite for this requirements can be found [here](https://github.com/ohduran/number_pi/blob/master/2.0/test-euler.py).

To do so, we must first define the `euler_term`, method, which takes i as an argument and returns the numerator and the denominator of the i-th term of the Euler series:

```python
from math import factorial
 # ...
def euler_term(self, i):
       """
       Obtain numerator and denominator
       of the i-th term in the Euler series.
       """
       f = factorial(i)
       numerator = (f * f) * pow(2, i+1)
       denominator = factorial(2 * i + 1)
       return numerator, denominator
```

That was easy.

Now, we instantiate the LongDecimalEuler class, inheriting from LongDecimal, and we instantiate it using the `as_quotient` method defined in `LongDecimal`. Numerator and denominator will be, of course, those calculated using the `euler_term` method that we spoke of before.

```python
def __init__(self, term=0, nodecimals=1):
    """Define constructor method."""
    # Avoid invalid input
    if not isinstance(term, int) or not isinstance(nodecimals, int):
        raise Exception('All inputs must be integers.')
    if term < 0:
            raise Exception('Parameter term must be positive.')
    if nodecimals < 0:
            raise Exception('Parameter nodecimals must be positive.')
    # Store the information provided
    self._term = term
    self._nodecimals = nodecimals
    # Calculate the Euler term
    numerator, denominator = self.euler_term(term)
    #Inherit from LongDecimal
    LongDecimal.__init__(self)

    # Define LongDecimalEuler as a quotient
    self.as_quotient(
            numerator=numerator,
            denominator=denominator,
            nodecimals=nodecimals)
```

## Compute Pi
Everything is now set: we have a pseudo-float number that is defined to have as many decimals as we please, and the necessary operations to compute are also in place.

It's time for the quarterback to throw the ball to the receiver. The definition of `compute_pi()` is as follows:

```python
#!environment/bin/python3
from longdecimals import LongDecimal
from euler import LongDecimalEuler


def compute_pi(nodecimals=0):
  # Exceptions for invalid input
    if not isinstance(nodecimals, int):
        raise Exception('The parameter nodecimals must be an integer.')
    if nodecimals < 0:
        raise Exception('The parameter nodecimals must be positive.')

    # If you are lazy enough to not provide decimals, I'm lazy enough too
    if nodecimals == 0:
        return LongDecimal(ciphers=[3])

    nodecimals += 2  # extra precision to avoid rounding up errors

    # set up ciphers for pi
    ciphers = [0] * (nodecimals + 1)

    # Define pi as a zero with a predefined number of decimals for efficiency
    pi = LongDecimal(
            ciphers=ciphers,
            negative=False)

    # First term
    term = 0
    euler_term = LongDecimalEuler(
        term=term,
        nodecimals=nodecimals)

    # Algorithm discussed above
    while not euler_term.iszero():
        pi = pi + euler_term

        term += 1

        euler_term = LongDecimalEuler(
            term=term,
            nodecimals=nodecimals)
    pi.setprecision(nodecimals - 2)

    return pi
```

>Spotted a mistake? Please send a PR, following the contribution guidelines stated [here](https://github.com/ohduran/number_pi/CONTRIBUTING.md)

>You want to add new functionality? Please see a list of tasks defined but not yet completed [here](https://github.com/ohduran/number_pi/blob/master/docs/ToDo.md)
