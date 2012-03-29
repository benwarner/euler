def list_divisors(n):
    """
    Returns a list of divisors of n.
    """

    divisors = [] 
    for k in range(n / 2 + 1)[1:]:
        if n % k == 0:
            divisors.append(k)
    divisors.append(n) # Because n counts as a divisor.

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


