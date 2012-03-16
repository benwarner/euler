# Find the largest palindrome made from the product of two 3-digit numbers.

best = 0
for j in range(1000)[::-1]:
    for i in range(1000)[::-1]:
        if i * j < best:
            break
        elif str(i * j) == str(i * j)[::-1]:
            best = i * j
        else:
            pass

print best
