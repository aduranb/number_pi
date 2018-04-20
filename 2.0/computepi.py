#!environment/bin/python3
from longdecimals import LongDecimal
from euler import LongDecimalEuler


def compute_pi(nodecimals=0):
    """
    Obtain the first nodecimals number of decimals
    of pi=3.1415... by aproximation using euler's formula:
    pi = infinity_sum(  (factorial(n)**2)*(2**(n+1)) / (factorial(2*n +1)) )

    http://mathworld.wolfram.com/PiFormulas.html
    """
    if not isinstance(nodecimals, int):
        raise Exception('The parameter nodecimals must be an integer.')
    if nodecimals < 0:
        raise Exception('The parameter nodecimals must be positive.')

    if nodecimals == 0:
        return LongDecimal(ciphers=[3])

    nodecimals += 2  # extra precision to avoid rounding up errors

    ciphers = [0] * (nodecimals + 1)

    pi = LongDecimal(
            ciphers=ciphers,
            negative=False)

    term = 0
    euler_term = LongDecimalEuler(
        term=term,
        nodecimals=nodecimals)

    while not euler_term.iszero():
        pi = pi + euler_term

        term += 1

        euler_term = LongDecimalEuler(
            term=term,
            nodecimals=nodecimals)
    pi.setprecision(nodecimals - 2)
    return pi
