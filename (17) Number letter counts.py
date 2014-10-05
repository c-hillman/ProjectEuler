#numtowords = {1: "one", 2: "two",
#              3: "three", 4: "four",
#              5: "five", 6: "six",
#              7: "seven", 8: "eight",
#              9: "nine", 10: "ten",
#              11: "eleven", 12: "twelve",
#              13: "thirteen", 14: "fourteen",
#              15: "fifteen", 16: "sixteen",
#              17: "seventeen", 18: "eighteen",
#              19: "nineteen", 20: "twenty",
#              30: "thirty", 40: "forty",
#              50: "fifty", 60: "sixty",
#              70: "seventy", 80: "eighty",
#              90: "ninety"}

numtolength = {1: 3,  2: 3,  3: 5,  4: 4,
               5: 4,  6: 3,  7: 5,  8: 5,
               9: 4,  10: 3, 11: 6, 12: 6,
               13: 8, 14: 8, 15: 7, 16: 7,
               17: 9, 18: 8, 19: 8, 20: 6,
               30: 6, 40: 5, 50: 5, 60: 5,
               70: 7, 80: 6, 90: 6}

oneTOnine = 0
for n in range(1, 10):
  oneTOnine += numtolength[n]

tenTOnineteen = 0
for n in range(10, 20):
  tenTOnineteen += numtolength[n]

twentyTOninetynine = 0
for n in range(20, 100, 10):
  twentyTOninetynine += numtolength[n]*10
  twentyTOninetynine += oneTOnine

onehundredTOninehundredandninetynine = 0
for n in range(1, 10):
  onehundredTOninehundredandninetynine += (numtolength[n]*100 + len("hundred")*100)
  onehundredTOninehundredandninetynine += (oneTOnine + len("and")*9)
  onehundredTOninehundredandninetynine += (tenTOnineteen + len("and")*10)
  onehundredTOninehundredandninetynine += (twentyTOninetynine + len("and")*80)

total = oneTOnine + tenTOnineteen + twentyTOninetynine + onehundredTOninehundredandninetynine
total += len("onethousand")

print(total)
