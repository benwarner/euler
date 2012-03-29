import math
import copy
 
#def phi(n):



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
        primes = genprimelisttd(math.sqrt(n), primes)

    factors = []
    while n > 1:
        i = 0
        try:
            while n % primes[i] != 0 and primes[i] <= math.sqrt(n):
                i += 1 
            if n % primes[i] == 0:
                factors.append(primes[i])
                n = n / primes[i]
            else: # We must have reached the square root.
                factors.append(n)
                break
        except IndexError as err:
            # We came just below the square root (e.g. 1693 is prime and math.sqrt(1693 == 41.146)
            factors.append(n)
            break

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


def genprimelisttd(maxprime, primes = [2, 3]):
    """
    Generates a list of primes by trial division.
    """
    
    if primes[0: 2] != [2, 3]: # Just a little data validation.
        primes=[2, 3]

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
