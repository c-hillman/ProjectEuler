from dwdiv import divisors

abundant = [n for n in range(12, 28124) if sum(divisors(n, False)) > n]
numbers = []

for n in abundant:
  for i in abundant:
    print(n, i)
    s = n + i
    if s not in numbers and s <= 28123:
      numbers.append(s)

print(sum(numbers))
