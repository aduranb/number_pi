#'''
#Numbers are arrays in which the 0-th digit as the integer part,
#and the following items are the n-1 decimal points (for an array of length n).
#'''


def sum_n_decimals(num1, num2):
    # "if the lists are not the same size, the function wont work"
    if len(num1) < len(num2):
        num1=num1+[0 for x in range(len(num1),len(num2))]
    elif len(num1) > len(num2):
        num2=num2+[0 for x in range(len(num2),len(num1))]

    n = len(num1)

    # Negative values: take all decimal points and make them negative too
    if num1[0] < 0 and num1[1]>0:
        for i in range(1, n):
            num1[i] = - num1[i]
    elif num2[0] < 0 and num2[1]>0:
        for i in range(1, n):
            num2[i] = - num2[i]

    # The sum per se: loops from the last decimal up to the first decimal,
    # making sure that no decimal is bigger than 10
    for i in xrange(n):
        # sum both and store them into num1
        num1[-i] += num2[-i]
        # what if, once we sum, that decimal point is more than 10 (carry over)
        while i != 0 and num1[-i] >= 10:
            num1[-i] -= 10
            num1[-i - 1] += 1
        # same if the decimal point is less than -10 (carry over)
        while i != 0 and num1[-i] <= -10:
            num1[-i] += 10
            num1[-i - 1] -= 1
    return num1


def prod_n_decimals(num1, num2):

    n = len(num1)
    # Negative values: take all decimal points and make them negative too
    if num1[0] < 0:
        for i in range(1, n):
            num1[i] = - num1[i]
    elif num2[0] < 0:
        for i in range(1, n):
            num2[i] = - num2[i]
    # multiply two decimals imply that the i-th and the j-th decimals considered
    # are multiplied and stored in the i+j-th position of the new number.
    # That means create a number num3 with length 2*n

    num3 = [0 for i in xrange(2 * n)]

    # the product
    for i in range(0, n):
        for j in range(0, n):
            num3[i + j] += num1[i] * num2[j]
    for i in xrange(1, 2 * n):
        # what if, once we sum, that decimal point is more than 10 (carry over)
        while num3[-i] >= 10:
            num3[-i] -= 10
            num3[-i - 1] += 1
        # same if the decimal point is less than -10 (carry over)
        while num3[-i] <= -10:
            num3[-i] += 10
            num3[-i - 1] -= 1
    return num3


def quot_n_decimals(num1, num2):
    n = max(len(num1),len(num2))
    num3 = [0 for x in range(n)]
    i = 0
    while i <n:
      q=0
      boo = True
      while boo:
        x = sum_n_decimals(num1,-1*num2)
        if x[0]>0:
          q += 1
          num1 = x
        else:
          bool = False
      num3[i]=q
      i+=1
    return num3



print quot_n_decimals([1,0,0,0,0,0,0],[3,0,0])
