a, b = 1, 1
count = 1
while len(str(a)) < 1000:
  a, b = b, a+b
  count += 1
print(count)
