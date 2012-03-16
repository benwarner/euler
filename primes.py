import math
import copy
 
#def phi(n):


def list_divisors(n):
    divisors = [] # Because n counts as a divisor.
    for k in range(n / 2 + 1)[1:]:
        if n % k == 0:
            divisors.append(k)
    divisors.append(n)

    return divisors


def tau(n):
    """
    Returns the number of divisors of n
    """

    factorlist = factorize(n)
    factor = factorlist[0]
    t = 1
    i = 1
    e = 2
    while i <= len(factorlist) - 1:
        if factor == factorlist[i]:
            e += 1
        else:
            t *= e
            e = 2
            factor = factorlist[i]
        i += 1
    t *= e

    return t


def list_factors(n, primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]):
    factors = recurfactorize(n, primes)
    factorstrlist = factors.split()
    factorlist = []
    for factor in factorstrlist:
        factorlist.append(int(factor))

    return factorlist

def recurfactorize(n, primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]):
    """
    Factorize by (recursive) trial division from a list of primes.
    """

    factors = ""

    if n == 1:
        return ""

    i = 0
    try:
        while primes[i] <= math.sqrt(n):
            if n % primes[i] == 0:
                factor = primes[i]
                break
            else:
                i += 1
        if primes[i] <= math.sqrt(n):
            factors += (" " + str(factor) + " " + str(factorize(n/primes[i], primes)))
            #factors.extend([factor, (factorize(n/primes[i], primes))])
            return factors
        else:
            return str(n)
    except IndexError:
        print "I'm sorry, but your list of primes is too short."
        return ""


def factorize(n, primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]):
    """
    Factorize by trial division from a list of primes.
    """
    
    if primes[-1] < math.sqrt(n):
        primes = genprimelistse(math.sqrt(n))
    factors = []
    i = 0
    n_original = copy.deepcopy(n)
    #print n_original
    try:
        while primes[i] <= math.sqrt(n_original) and n > 1:
            if n % primes[i] == 0:
                factors.append(primes[i])
                #print 'primes[i] = %d' % primes[i]
                #print 'n = %d' % n
                n = n / primes[i]
                #print 'n = %d' % n
            else:
                i += 1
    except IndexError:
        print "I'm sorry, but your list of primes is too short."
        return []
    if n != 1:
        factors.append(primes[i])
    return factors

def isprime(n):
    """
    Checks if n is prime by one iteration of Fermat's little theorem.
    """

    return True if 2 ** (n - 1) % n == 1 else False


def genprimelistflt(maxprime, primes = [2, 3]):
    """
    Generates a list of primes by Fermat's little theorem.
    """

    n = primes[::-1][0]
    while n <= maxprime:
        if isprime(n):
            primes.append(n)
        n = n + 2

    return primes 


def genprimelistse(maxprime, primes = [2, 3]):
    """
    Generates a list of primes by the sieve of Eratosthenes.
    """

    n = primes[::-1][0] + 2
    while n <= maxprime:
        prime = True
        i = 0
        while primes[i] <= math.sqrt(n):
            if n % primes[i] == 0:
                prime = False
                break
            i += 1
        if prime:
            primes.append(n)
        n = n + 2

    return primes 
