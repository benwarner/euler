from math import factorial

def permutation(items, n):
    """
    items is a sequential object of items to permute.
    Returns the nth (zero based) lexicographic permutation of that iterable as a list.
    """
    
    try:
        items = list(items)
    except TypeError:
        return TypeError

    n = n % factorial(len(items))
    orderlist = []
    for k in range(len(items))[::-1]:
        orderlist.append(n // factorial(k))
        n = n % factorial(k)
    
    permuteditems = []
    for i in orderlist:
        permuteditems.append(items.pop(i))

    return permuteditems
