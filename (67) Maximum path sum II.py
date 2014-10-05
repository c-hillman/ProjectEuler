triangle = [[int(n) for n in row.split(" ")] for row in str(open("(67) triangle.txt").read().replace("\n", "|")).split("|")]

for n in range(len(triangle)-2, 0-1, -1):
    for x in range(0, len(triangle[n])):
        triangle[n][x] += max(triangle[n+1][x], triangle[n+1][x+1])

print(triangle[0][0])
