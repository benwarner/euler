from primes import prime_powers

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

    prime_power_list = prime_powers(n)
    t = 1
    for e in prime_power_list:
        t *= e[1] + 1

    return t


