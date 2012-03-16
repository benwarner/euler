# What is the largest prime factor of the number 600851475143?

import primes

plist = primes.genprimelistse(10000)
factorlist = primes.listfactors(600851475143, plist)
print factorlist
