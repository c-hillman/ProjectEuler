#Number of routes is (a+b)Ca (combinatorics) where
#the grid is of dimensions a x b.
#Note: nCr = n!/(r!(n-r)!)

from math import factorial

h, v = 20, 20 #dimensions - horizontal/vertical
routes = int(factorial(h+v)/(factorial(h)*factorial(v)))
print(routes)
