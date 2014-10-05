from dwdiv import divnum

i, n = 1, 1#first triangle number
while divnum(n) < 500:
  i += 1
  n += i
print(n)
