import dwdiv

def d(n):
    return sum([x for x in range(1, int(n/2) + 1) if n%x == 0])

limit = 10000
total = 0
primes = dwdiv.Eratos(limit)

for a in range(1, limit):
    if a not in primes:
        b = d(a)
        if a == d(b) and a != b:
            total += a + b
            primes.append(b)

print(total)
