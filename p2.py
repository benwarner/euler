# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a1 = 1
a2 = 1 + a1
total = 0

while a2 <= 4000000:
    if a2 % 2 == 0:
        total += a2
    a1, a2 = a2, a1 + a2

print total
