# Creating classes and methods that fits calculation of a large set of decimals. #

class BigNo:
    """ This class stores a number with a large set of decimals.
    
    ## Keyword arguments ##
    ciphers    --   The list of ciphers available for the BigNo. The first is the integer, and won't carry over.
    
    nodecimals --   (default as len(ciphers) - 1  -- The number of decimals. Can be set differently from default.
    
    negative   --   (default as positive = False) -- True if negative, False if positive
    
    
    ## Key features ##
    carry over    --    no cipher c will be outside [0,9], and they will always be integers.
                        if c >= 10, then will carry over onto the next position until c in [0,9].
                        cipher can acommodate integers outside [0,9], but will be displayed
                        as numbers in [0,9].
    
    nodecimals    --   BigNo accomodates a different number of decimals other than the length of
                       ciphers. It will simply add zeros at the end of ciphers until the number
                       of decimals is what was input; or constrain the length of ciphers up until
                       the first (nodecimals + 1) ciphers.
    
    
    ## Key methods ##
                       
    iszero        --    if all ciphers are zero, then iszero = True; else, False.
                    
    setnodecimals --    nodecimals can be changed with this method, thus changing ciphers list.
    
    setpositive   --    set the number as positive (True) or negative (False).
    
    overten       --    divide the number by 10, moving all ciphers one decimal point behind.
                        if keeplast = True (default as False), then nodecimals += 1,
                        else it remains constant.
    
    displayBigNo  --    presents the number as a string in a readable fashion way
                        
    ## Exceptions ##
    
    Problems are reported in 3 parts: context, problem & solution.
    Here's a few examples.
    
        Context:    Saving connection pooling configuration changes to disk.
        Problem:    Write permission denied on file '/xxx/yyy'.
        Solution:   Grant write permission to the file.
        
        Context:    Sending email to 'abc@xyz.com' regarding 'Blah'.
        Problem:    SMTP connection refused by server 'mail.xyz.com'.
        Solution:   Contact the mail server administrator to report a service problem.
                    The email will be sent later. You may want to tell 'abc@xyz.com' about this problem.

    """

    def __init__(self, ciphers, nodecimals=None, negative=False):

        if not isinstance(ciphers, list):
            raise Exception(
                '"ciphers" stores the list of ciphers and is expected to be a list, which is not the case. Try using a list of integers')
        else:
            for i in range(len(ciphers)):
                if not isinstance(ciphers[i], int):
                    raise Exception(
                        'Some of the items in "ciphers" are not integers, and that is not consistent with the definition of BigNo. Try using a list of integers.')

        if not isinstance(nodecimals, int) and nodecimals != None:
            raise Exception(
                'The number of decimal points is expected to be an integer. Try using an integer, or leave it blank [optional field]')

        if not isinstance(negative, bool):
            raise ('negative is expected to be a boolean. Try using True [BigNo < 0] or False [BigNo > 0].')

        self.negative = negative

        self.ciphers = ciphers
        for i in xrange(1, len(ciphers)):
            while self.ciphers[-i] >= 10:
                self.ciphers[-i] -= 10
                self.ciphers[-i - 1] += 1
            while self.ciphers[-i] < 0:
                self.ciphers[-i] += 10
                self.ciphers[-i - 1] -= 1

        if nodecimals == None:
            self.nodecimals = len(ciphers) - 1
        else:
            self.nodecimals = nodecimals
            if nodecimals > len(ciphers) - 1:
                ciphers = ciphers + [0] * (nodecimals - len(ciphers) + 1)
            elif nodecimals < len(ciphers) - 1:
                ciphers = ciphers[:nodecimals + 1:]
            self.ciphers = ciphers

    def iszero(self):
        return sum([1 for i in range(0, len(self.ciphers)) if self.ciphers[i] == 0]) == len(self.ciphers)

    def setnodecimals(self, nodecimals):
        if nodecimals > self.nodecimals:
            self.ciphers = self.ciphers + [0] * (nodecimals - self.nodecimals)
            self.nodecimals = nodecimals
        else:
            self.ciphers = self.ciphers[:nodecimals + 1:]
            self.nodecimals = nodecimals
        return self

    def setpositive(self, bool=True):
        self.negative = not bool
        return self

    def overten(self, keeplast=False):
        self.ciphers.insert(0, 0)
        if not keeplast:
            self.ciphers.pop()
        return self

    def displayBigNo(self):
        if self.negative:
            return "-", str(self.ciphers[0]) + "." + ''.join(
                [str(self.ciphers[i]) for i in range(1, self.nodecimals + 1)])
        else:
            return str(self.ciphers[0]) + "." + ''.join([str(self.ciphers[i]) for i in range(1, self.nodecimals + 1)])


class BigInt(BigNo):
    """ This class stores an integer number with a large set of decimals. It inherits from BigNo class.

        ## Keyword arguments ##
        number    --   The integer number that identifies this BigNo.

        nodecimals --   (default as 1)  -- The number of decimals.

        negative   --   (default as positive = False) -- True if negative, False if positive


        ## Key features ##

        nodecimals    --   BigNo accomodates a different number of decimals other than the length of
                           ciphers. It will simply add zeros at the end of ciphers until the number
                           of decimals is what was input; or constrain the length of ciphers up until
                           the first (nodecimals + 1) ciphers.


        ## Key methods ##

        iszero        --    if all ciphers are zero, then iszero = True; else, False.

        setnodecimals --    nodecimals can be changed with this method, thus changing ciphers list.

        setpositive   --    set the number as positive (True) or negative (False).

        overten       --    divide the number by 10, moving all ciphers one decimal point behind.
                            if keeplast = True (default as False), then nodecimals += 1,
                            else it remains constant.

        displayBigNo  --    presents the number as a string in a readable fashion way

        ## Exceptions ##

        Problems are reported in 3 parts: context, problem & solution.
        Here's a few examples.

            Context:    Saving connection pooling configuration changes to disk.
            Problem:    Write permission denied on file '/xxx/yyy'.
            Solution:   Grant write permission to the file.

            Context:    Sending email to 'abc@xyz.com' regarding 'Blah'.
            Problem:    SMTP connection refused by server 'mail.xyz.com'.
            Solution:   Contact the mail server administrator to report a service problem.
                        The email will be sent later. You may want to tell 'abc@xyz.com' about this problem.

        """

    def __init__(self, number, nodecimals=1, negative=False):
        if not isinstance(number, int):
            raise Exception(
                'The number you have introduced is not an integer. Please introduce a valid integer number.')

        ciphers = [number, 0]

        if not isinstance(nodecimals, int):
            raise Exception(
                'The number of decimal points is expected to be an integer. Try using an integer, or leave it blank [optional field]')

        if not isinstance(negative, bool):
            raise (
            'negative is expected to be a boolean. Try using True [BigNo < 0], False [BigNo > 0] or leave it blank (will assume False).')

        BigNo.__init__(self, ciphers, nodecimals, negative)
        if nodecimals != 1:
            self.setnodecimals(nodecimals)


def BigNo_bigger_module(x, y):
    """ This function makes out which BigNo is bigger in module, regardless of negative/positive
    
        ## Keyword arguments
        
        x -- BigNo number 0
        y -- BigNo number 1
        
        ## Use case
        
        For each position i in x's and y's ciphers, if x's is bigger, then return 0,
        if y's is bigger, return 1. If that is not the case, move onto the next position.
        Once we reach the final position, and still x's == y's,
        then return 2, meaning "their modules are the same".
    
    """
    if not isinstance(x, BigNo) or not isinstance(y, BigNo):
        raise Exception('Some of the arguments are not BigNo class. Use instances of BigNo as arguments in both cases.')

    i = 0
    while True:
        if x.ciphers[i] > y.ciphers[i]:
            return 0
        elif x.ciphers[i] < y.ciphers[i]:
            return 1
        elif i == min(y.nodecimals, x.nodecimals):
            return 2
        else:
            i += 1


def BigNo_sum(x, y, nodecimals=None):
    """ This function takes two BigNo, and returns the sum of them as BigNo class.

        ## Keyword arguments

        x -- BigNo number 0
        y -- BigNo number 1
        
        ## Use case

        For each position i in x's and y's ciphers, if x's is bigger, then return 0,
        if y's is bigger, return 1. If that is not the case, move onto the next position.
        Once we reach the final position, and still x's == y's,
        then return 2, meaning "their modules are the same".

    """

    if not isinstance(x, BigNo) or not isinstance(y, BigNo):
        raise Exception('Some of the arguments are not BigNo class. Use instances of BigNo as arguments in both cases.')

    if not isinstance(nodecimals, int) and nodecimals != None:
        raise Exception(
            'The number of decimal points is expected to be an integer. Try using an integer, or leave it blank [optional field]')

    if nodecimals == None:
        nodecimals = max(x.nodecimals, y.nodecimals)

    x_ = BigNo(ciphers=x.ciphers, negative=x.negative, nodecimals=nodecimals)  # do not use x_=x, that wont work
    y_ = BigNo(ciphers=y.ciphers, negative=y.negative, nodecimals=nodecimals)

    aux = {0: [x_.negative, x_.ciphers],
           1: [y_.negative, y_.ciphers]
           }

    cero_one = BigNo_bigger_module(x_, y_)

    if cero_one == 0:
        # the first one is bigger
        if aux[0][0]:
            # the first one is negative
            negative = True  # in any case, the result is going to be negative
            if aux[1][0]:
                # the second one is also negative
                ciphers = [x_.ciphers[i] + y_.ciphers[i] for i in range(nodecimals + 1)]
            else:
                # the second one is positive
                ciphers = [x_.ciphers[i] - y_.ciphers[i] for i in range(nodecimals + 1)]
        else:
            # the first one is positive
            negative = False  # in any case, the result is going to be positive
            if aux[1][0]:
                # the second one is  negative
                ciphers = [x_.ciphers[i] - y_.ciphers[i] for i in range(nodecimals + 1)]
            else:
                # the second one is also positive
                ciphers = [x_.ciphers[i] + y_.ciphers[i] for i in range(nodecimals + 1)]
    elif cero_one == 1:
        # the second one is bigger
        if aux[1][0]:
            # the second one is negative
            negative = True  # in any case, the result will be negative
            if aux[0][0]:
                # the first one is also negative
                ciphers = [y_.ciphers[i] + x_.ciphers[i] for i in range(nodecimals + 1)]
            else:
                # the first one is positive
                ciphers = [y_.ciphers[i] - x_.ciphers[i] for i in range(nodecimals + 1)]
        else:
            # the second one is positive
            negative = False  # in any case, the result will be positive
            if aux[0][0]:
                # the first one is  negative
                ciphers = [y_.ciphers[i] - x_.ciphers[i] for i in range(nodecimals + 1)]
            else:
                # the first one is also positive
                ciphers = [y_.ciphers[i] + x_.ciphers[i] for i in range(nodecimals + 1)]
    else:
        # they are the same size
        if aux[0][0]:
            # the first one is negative
            negative = True  # its either zero or negative
            if aux[1][0]:
                # the second one is also negative
                ciphers = [x_.ciphers[i] + y_.ciphers[i] for i in range(nodecimals + 1)]
            else:
                # the second one is positive
                ciphers = [x_.ciphers[i] - y_.ciphers[i] for i in range(nodecimals + 1)]
        else:
            # the first one is positive
            negative = False  # its either zero or positive
            if aux[1][0]:
                # the second one is  negative
                ciphers = [x_.ciphers[i] - y_.ciphers[i] for i in range(nodecimals + 1)]
            else:
                # the second one is also positive
                ciphers = [x_.ciphers[i] + y_.ciphers[i] for i in range(nodecimals + 1)]

    return BigNo(ciphers=ciphers, negative=negative)


def BigNo_product(x, y, nodecimals=None):
    """ This function takes two BigNo, and returns the product of them as BigNo class.

            ## Keyword arguments

            x           --  BigNo number 0
            y           --  BigNo number 1
            nodecimals  --  the predefined integer number of decimals for the resulting BigNo;.
                            if None, then it will be the sum of x and y's decimals.
            
            ## Use case

            Sign is always going to be negative if one of them is negative,
            and positive if either both are negative or both are positive.
            
            The cipher list product will take in position i+j 
            the product of x's i-th cipher and y's j-th cipher.

    """

    if not isinstance(x, BigNo) or isinstance(y, BigNo):
        raise Exception('Some of the arguments are not BigNo class. Use instances of BigNo as arguments in both cases.')

    if not isinstance(nodecimals, int) and not isinstance(nodecimals, None):
        raise Exception(
            'The number of decimal points is expected to be an integer. Try using an integer, or leave it blank [optional field]')

    negative = x.negative and not y.negative or not x.negative and y.negative

    product = [0] * (x.nodecimals + y.nodecimals + 1)

    for i in range(x.nodecimals + 1):
        for j in range(y.nodecimals + 1):
            product[i + j] += x.ciphers[i] * y.ciphers[j]

    return BigNo(ciphers=product, negative=negative).setnodecimals(nodecimals)


def BigNo_quotient(x, y, nodecimals=None):
    """ This function takes two BigNo, and returns the quotient of them as BigNo class up to a decimal point.

                ## Keyword arguments

                x           --  BigNo dividend
                y           --  BigNo divisor
                nodecimals  --  the predefined integer number of decimals for the resulting BigNo;.
                                if None, then it will be the max of x and y's decimals.

                ## Use case

                Sign is always going to be negative if one of them is negative,
                and positive if either both are negative or both are positive.
                
                We created auxiliar x called x_ that will be reduced to zero
                by means of substracting y a number q of times for each position i
                (just like in school).
                
                If the auxiliar x_ is less than y, then q is stored as
                the final quotient cipher, and we move onto the next while dividing y over ten (keep decimal numbers).,
                so that we are substracting using the correct cipher.
                
                This will happen up until we reach the number of decimals that we aimed for.

        """

    if not isinstance(x, BigNo) or not isinstance(y, BigNo):
        raise Exception('Some of the arguments are not BigNo class. Use instances of BigNo as arguments in both cases.')

    if not isinstance(nodecimals, int) and nodecimals != None:
        raise Exception(
            'The number of decimal points is expected to be an integer. Try using an integer, or leave it blank [optional field]')

    if nodecimals == None:
        nodecimals = max(x.nodecimals, y.nodecimals)
    negative = x.negative and not y.negative or not x.negative and y.negative

    x_ = BigNo(ciphers=x.ciphers, negative=False).setnodecimals(nodecimals)
    y_ = BigNo(ciphers=y.ciphers, negative=True).setnodecimals(nodecimals)

    ciphers = [0] * (nodecimals + 1)

    i = 0
    while not sum(y_.ciphers[:nodecimals + 1:]) == 0:
        z = BigNo_sum(x_, y_)
        q = 0
        while BigNo_bigger_module(x_, y_) == 0:
            q += 1
            x_ = z
            z = BigNo_sum(x_, y_)
        ciphers[i] = q
        y_ = y_.overten(True)
        i += 1
    return BigNo(ciphers=ciphers, negative=negative, nodecimals=nodecimals)
