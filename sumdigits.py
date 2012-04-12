def sumdigits(number):
    total = 0
    for d in str(long(number)):
        total += int(d)

    return total

