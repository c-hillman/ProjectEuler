names = open("(22) names.txt").read().split("\",\"")
names[0], names[5162] = "MARY", "ALONSO"
names.sort()
total = 0
alphabet = {'M': 13, 'L': 12, 'O': 15, 'N': 14,
            'I': 9, 'H': 8, 'K': 11, 'J': 10,
            'E': 5, 'D': 4, 'G': 7, 'F': 6,
            'A': 1, 'C': 3, 'B': 2, 'Y': 25,
            'X': 24, 'Z': 26, 'U': 21, 'T': 20,
            'W': 23, 'V': 22, 'Q': 17, 'P': 16,
            'S': 19, 'R': 18}

for name in names:
    alph = 0
    for letter in list(name):
        alph += alphabet.get(letter)
    total += alph * (names.index(name) + 1)

print(total)
