# '''
# Numbers are arrays in which the 0-th digit as the integer part,
# and the following items are the n-1 decimal points (for an array of length n).
# '''


def carry_over(num1):
    """
    When we sum, or multiply, we have to carry over 1 or more to the upper
    #decimal point when the decimal point is 10 or more (or -10 or less)
    :type: (list) -> list
    :param num1: the number without carry over
    :return: the number in the correct format
    """
    n = len(num1)
    for i in range(n):
        # if the decimal point is 10 or more (carry over)
        while num1[-i] >= 10:
            num1[-i] -= 10
            num1[-i - 1] += 1
        # same if the decimal point is -10 or less (carry over)
        while i < n and num1[-i] <= -10:
            num1[-i] += 10
            num1[-i - 1] -= 1
    return num1


def sum_n_decimals(num1, num2, n=None):
    """
    :type: (list,list,list) -> list
    :param num1: big number with 0-th as the integer and the rest as decimal points
    :param num2: big number with 0-th as the integer and the rest as decimal points
    :param n: length of the resultant sum of numbers; maximum length of num1/num2 by default
    :return: sum of num1 and num2 in the same format
    """
    if n is None or type(n) != int:
        n = max(len(num1), len(num2))
    # if you want to substract instead of sum, make sure all positions are negative.

    fin_num = [0] * n  # where we are storing the sum

    # The sum per se: loops from the last decimal up to the first decimal,
    # making sure that no decimal is bigger than 10
    for i in xrange(n):
        # sum both and store them into num1
        fin_num[-i] += num2[-i] + num1[-i]

    # and now, we carry over the result to avoid decimal points with a value outside [-9,9]
    fin_num = carry_over(fin_num)
    return fin_num


def prod_n_decimals(num1, num2, n=None):
    """
    :type: (list,list,int) -> list
    :param num1: big number with 0-th as the integer and the rest as decimal points
    :param num2: big number with 0-th as the integer and the rest as decimal points
    :param n: length of the resultant product of numbers; maximum length of num1/num2 by default
    :return: product of num1 and num2 in the same format
    """
    # This will cover the default functionality of n
    if n is None or type(n) != int:
        n = max(len(num1), len(num2))

    # multiply two decimals imply that the i-th and the j-th decimals considered
    # are multiplied and stored in the i+j-th position of the new number.

    num3 = [0] * n

    # the product
    i = 0
    j = 0
    while i < n:
        while j < n - i:
            num3[i + j] += num1[i] * num2[j]

            j += 1
        i += 1

    # and now, we carry over the result to avoid decimal points with a value outside [-9,9]
    num3 = carry_over(num3)
    return num3


def one_over_n_decimals(num, n):
    """
    :type: (int,int) -> list
    :param num: the number to which we divide 1
    :param n: the length of the outcoming number-list
    :return: the resulting quotient in number-list format
    """
    # We create the array in which we are storing the final quotient
    array = [0] * n

    # divide 1 over a certain number and store in the array.
    # 0-th is the integer, the followings are the decimal points.

    x = 1  # the initial number is obviously 1

    # filling the array until the end
    i = 0
    while i < n:
        # the quotient will be divide what we have in x over num
        q = x / num
        # and the rest will be stored as x for the next decimal point
        r = x % num
        # lets do so
        array[i] = q
        x = r * 10
        i += 1
    return array


def quotient_n_decimals(numerator, denominator, n):
    """
        :type: (int,int) -> list
        :param numerator: the number to which we divide 1
        :param denominator: the number to which we divide 1
        :param n: the length of the outcoming number-list
        :return: the resulting quotient in number-list format
        """
    # We create the array in which we are storing the final quotient
    array = [0] * n

    # divide numerator over a denominator and store in the array.
    # 0-th is the integer, the followings are the decimal points.

    x = numerator  # the initial number is obviously numerator

    # filling the array until the end
    i = 0
    while i < n:
        # the quotient will be divide what we have in x over num
        q = 0
        while x > denominator:
            x -= denominator
            q += 1

        # and the rest will be stored as x for the next decimal point
        # lets do so
        array[i] = q
        x *= 10
        i += 1
    return array
