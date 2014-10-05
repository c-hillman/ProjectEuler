def fib(n): #n max number
  total = 0
  a, b = 1, 2
  while a < n:
    if a%2 == 0:
      total += a
    a, b = b, a + b
  return total

print(fib(4000000))
  
  
