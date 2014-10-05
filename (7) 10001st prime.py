def isPrimeAbove3(n):
  for x in range(3, int(n**0.5 + 1), 2):
    if n%x == 0: return False
  return True

n = 3
count = 1

while n:
  if isPrimeAbove3(n):
    count += 1
    if count == 10001:
      print(n)
      break
  n += 2
