biggest = 0
for n1 in range(999, 100, -1):
  for n2 in range(n1, 100, -1):
    n = n1 * n2
    if str(n) == str(n)[::-1] and n > biggest:
      biggest = n
      break
print(biggest)
