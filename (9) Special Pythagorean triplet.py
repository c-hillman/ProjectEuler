#For a Pythagorean triplet, a = m**2 - n**2
#                           b = 2mn           for positive integers m > n
#                           c = m**2 + n**2
#But 0 < a <= 499 (as a + b + c = 1000 and c > a)
# so 0 < n < m <= sqrt(499), m <= 22

#a + b + c = 1000
#Therefore, 2m**2 + 2mn = 1000
#           m**2 + mn = 500
#Find: abc = 2m**5n - 2mn**5

def findMN():
  for m in range(2, 23): #lowest value of m is 2 as 0 < n < m (integers)
    for n in range(1, m): #m > n
      if m**2 + m*n == 500: #only one value of m and n fit all conditions
        return m, n

m, n = findMN()
abc = 2*m**5*n - 2*m*n**5
print(abc)
