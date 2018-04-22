# http://mathworld.wolfram.com/PiFormulas.html

# eulers formula is as follows:
# pi = infinity_sum(  (factorial(n)**2)*(2**(n+1)) / (factorial(2*n +1)) )

from n_decimals_operations import sum_n_decimals, quotient_n_decimals


def is_null(l):
    """
    This function will return True only if all the elements on a list are zero
    :type: (list) -> bool
    :param l: a number-list
    :return: True only if the list is complete with zeros
    """
    for element in l:
        if element != 0:
            return False
    return True


def factorial(n):
    """
    Used iteration to create factorial = n*(n-1)*(n-2)* ... 1
    Avoid runtime error for big numbers using iteration
    :type: (int) -> int
    :param n: the n-th term
    :return: the factorial 
    """
    try:
        # Use recursion generally
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


def euler_pi(i, n):
    """
    The i-th of the Euler sequence that add up pi
    :type: (int, int) -> list
    :param i: the i-th terms index
    :param n: the length of the big number
    :return: the i-th euler term
    """
    # Avoid unnecessary calculations by storing factorial i as f
    f = factorial(i)
    # Make use of quotient_n_decimals to transform the division into number_list format
    return quotient_n_decimals((f * f) * pow(2,i+1), factorial(2 * i + 1), n)


def number_pi_euler(dec_points):
    """
    Obtain the number pi as a number list with dec_points decimal points
    :param dec_points: decimal points
    :return: number pi in big number list format
    :rtype: list
    """

    # set up the array in which we are storing the number (include the integer as a position)
    dec_points += 1
    pi = [0] * dec_points

    # The first term will be
    i = 0
    term = euler_pi(i, dec_points)
    # And then, while the next term is not a complete sequence of zeros...
    while not is_null(term):
        # add up to the pi list the next term
        pi = sum_n_decimals(pi, term, dec_points)
        # and calculate the next term for the next iteration
        # also to see if it is_null or not
        i += 1
        term = euler_pi(i, dec_points)
    return pi
