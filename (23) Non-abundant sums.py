from datetime import datetime
startTime = datetime.now()

def divisors(n):
    return [x for x in range(1, int(n/2) + 1) if n%x == 0]

abundant = [n for n in range(12, 28124) if sum(divisors(n)) > n]
numbers = list(range(12, 28124))

print("Starting iterative process...")

for n in abundant:
  for i in abundant[abundant.index(n):]:
    s = n + i
    if s in numbers:
 print(sum(numbers))
print(datetime.now()-startTime)
