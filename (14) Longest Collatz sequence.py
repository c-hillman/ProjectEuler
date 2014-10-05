def findCollatzLength(n):
  length = 1
  i = n
  while i > 1:
    if i%2 == 0: i = int(i/2)
    else: i = i*3+1
    if i in knownLengths:
      length += knownLengths[i]
      knownLengths[n] = length 
      return length
    length += 1
  knownLengths[n] = length
  return length
    

knownLengths = {}

longest = [1, 1] #[n, length] - tuple does not support assignment
for n in range(2, 1000000):
  length = findCollatzLength(n)
  if length > longest[1]: longest = [n, length]
print(longest[0])
