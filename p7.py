# What is the 10 001st prime number?

import primes

plist = primes.genprimelistse(150000) 
    # That should be big enough to get the prime I need.
print len(plist)
print plist[10000] # Remember that Python is zero based.
