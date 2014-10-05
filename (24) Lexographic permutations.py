def isPerm(n):
  n = str(n)
  for i in numbers:
    if i not in n:
      return False
  return True

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
permutations = [n for n in range(123456789, 9876543210+1) if len(str(n)) == len(set(str(n)))]
print(permutations[999999])
