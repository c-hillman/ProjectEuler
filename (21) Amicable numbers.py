def isAmicable(a):
  b = sumOfDivisors(a)
  if a == sumOfDivisors(b) and a != b:
    return b
  return False

def sumOfDivisors(n):
  return sum([x for x in range(1, int(n/2) + 1) if n%x == 0])

amicableTotal = 0
numbers = list(range(1, 10000))
for n in numbers:
  b = isAmicable(n)
  if b:
    amicableTotal += n
    if b in numbers: numbers.remove(b)
    if b < 10000: amicableTotal += b

print(amicableTotal)
