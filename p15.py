# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner. How many routes are there through a 20x20 grid?

from math import factorial

print factorial(40)/(factorial(20)*factorial(20))
