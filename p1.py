# Add all the natural numbers below one thousand that are multiples of 3 or 5.
total = 0
for i in range(1000):
    if (i % 3 == 0) | (i % 5 == 0):
        total += i
print total

# now let's do this by the formula:
formula =  3*.5*333*334 + 5*.5*199*200 -15*.5*66*67

print formula
