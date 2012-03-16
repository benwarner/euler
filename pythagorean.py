"""
Work with pythagorean triples.
"""

def make_triple(m, n, k=1):
    """
    In the triple a**2 + b**2 = c**2:
    a = m**2 - n**2
    b = 2mn
    c = m**2 + n**2
    k is a scaling factor. (k*a, k*b, k*c) is also a triple.
    """

    return (k * (m**2 - n**2), k * 2*m*n, k * (m**2 + n**2))
