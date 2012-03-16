# What is the value of the first triangle number to have over five hundred divisors?

from primes import *
from triangular import triangular

plist = genprimelistse(100000)
n = 5025
t = triangular(n)
while count_divisors(t) <= 500:
    # you must have at least 9 factors to have 500 divisors.
    incremented = False
    while (len(list_factors(t, plist)) < 11) or (len(set(list_factors(t, plist))) < 9): 
        n += 1
        incremented = True
        t = triangular(n)
    if not incremented:
        n += 1
        t = triangular(n)
    print n

print (list_divisors(t))
