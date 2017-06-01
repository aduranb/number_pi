import bigno as bn
from operator import add


# http://mathworld.wolfram.com/PiFormulas.html

# eulers formula is as follows:
# pi = infinity_sum(  (factorial(n)**2)*(2**(n+1)) / (factorial(2*n +1)) )

def factorial(n):
    """ This function takes an integer n, and returns the factorial of n as an integer.

        ## Keyword arguments

        n -- integer positive number
        
        ## Use case

        Recursively calculates the factorial of a number up until RunTimeError,
        when calculates the rest iteratively.
        n! = n * (n-1) * ... * 1
    """
    if not isinstance(n, int):
        raise Exception('The input is either not an integer. Please choose a valid number.')
    if n < 0:
        raise Exception('The number you have chosen is negative. Please choose a positive number.')
    try:
        # Use recursion whenever possible
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    # Perform iteration to avoid stack overflow
    except RuntimeError:
        f = 1
        i = 1
        while i < n:
            f *= i
            i += 1
        return f


def euler_pi(n, nodecimals=1):
    """ This function takes an integer n, and returns the factorial of n as an integer.

        ## Keyword arguments

        n           -- the index of the element in the Euler series
        nodecimals  -- the number of decimals, defaulted as 1.
        
        ## Use case

        It calculates the i-th element in the Euler series and returns
        that element in the form of a BigNo instance.
    """

    if not isinstance(n, int):
        raise Exception('The input is either not an integer. Please choose a valid number.')
    if n < 0:
        raise Exception('The number you have chosen is negative. Please choose a positive number.')

    # Avoid unnecessary calculations by storing n! as f
    f = factorial(n)

    # Set the numerator and denominator of the number
    numerator = (f * f) * pow(2, n + 1)
    denominator = factorial(2 * n + 1)
    # We create the array in which we are storing the final quotient
    ciphers = []

    # divide numerator over a denominator and store in the array.
    # 0-th is the integer, the followings are the decimal points.

    x = numerator  # the initial number is obviously numerator

    # filling the array until the end
    i = 0
    while i < nodecimals + 10:
        # the quotient will be divide what we have in x over num
        q = 0
        while x >= denominator:
            x -= denominator
            q += 1

        # and the rest will be stored as x for the next decimal point
        ciphers.append(q)
        x *= 10
        i += 1

    # Rounding up: the last 3 ciphers will determine whether we increase or decrease the last decimal point.
    for i in range(1, 10):
        if ciphers[-i] > 4:
            ciphers[-i - 1] += 1

    return bn.BigNo(ciphers=ciphers[:nodecimals + 1:], nodecimals=nodecimals, negative=False)


def number_pi(nodecimals=4, method='euler'):
    """This function calculates the number pi up to the first nodecimals decimal points, using a certain method.

        ## Keyword arguments

        nodecimals  -- the number of decimals, defaulted as 4 (you should expect 3.1415).
        method      -- the method used, defaulted as euler
        
        ## Use case

        It calculates pi as an infinite number, capped up until the point in which the next term's first "nodecimal"
        decimal points are zero, and provides the result as a BigNo instance.
        
        WARNING:    This method does not take into account whatever comes after the last decimal point considered.
                    That's why the last cipher may differ from the real one. As long as we increase the decimal
                    points, actual ciphers will arise.
    
    """
    methods = ['euler']
    if method not in methods:
        raise Exception('Choose a valid method from the following list: {0}'.format(" , ".join(methods)))

    # set up the array in which we are storing the number (include the integer as a position)

    pi = [0] * (nodecimals + 1)

    if method == 'euler':
        # The first term will be
        i = 0
        term = euler_pi(i, nodecimals=nodecimals)
        # And then, while the next term is not a complete sequence of zeros...
        while not term.iszero():
            # add up to the pi list the next term
            t = term.ciphers

            # pi[i] = pi[i] + t[i]
            pi = map(add, pi, t)

            # and calculate next steps
            i += 1
            term = euler_pi(i, nodecimals=nodecimals)
        return bn.BigNo(ciphers=pi, nodecimals=nodecimals)
