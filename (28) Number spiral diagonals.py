total = n = 1
increment = 0
while n < 1001**2:
  increment += 2
  for i in range(0, 4): #repeat 4 times
    n += increment
    total += n
print(total)
