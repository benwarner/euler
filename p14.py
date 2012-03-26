# Find the longest chain in the collatz problem where the starting number is less than one million.

best = 1

for n in range(1000001)[1:]:
    k = n
    chain = 1
    while k != 1:
        if k % 2 == 0:
            k = k / 2
        else:
            k = 3 * k + 1
        chain += 1
    if chain >= best:
        best = chain
        king_o_da_hill = n

print 'starting number % d' % king_o_da_hill
print 'chain length % d' % best
