import random


# min for height and width = 6
HEIGHT = 35
WIDTH = HEIGHT
SOLUTION = [1, 0, 1, 2, 2, 1]

# create NxN list
# fill it random with 0,1,2
matrix = [[random.randint(0,2) for x in range(WIDTH)] for y in range(HEIGHT)]

# check horizontal for SOLUTION
count = 0
row_num = 0
for row in matrix:
    print(row)
    for i in range(WIDTH-6):
        if row[i:i+6] == SOLUTION:
            count +=1
            print(f"horizontal, x={i}, y={row_num}")
    row_num += 1

# check vertical for SOLUTION
for x in range(WIDTH):
    for y in range(HEIGHT-6):
        if [matrix[y][x],
            matrix[y+1][x],
            matrix[y+2][x],
            matrix[y+3][x],
            matrix[y+4][x],
            matrix[y+5][x]] == SOLUTION:
            count +=1
            print(f"vertical, x={x}, y={y}")

# check diagonal for SOLUTION
for y in range(HEIGHT - 6):
    for i in range(max(HEIGHT, WIDTH) - 6 - y):
        if [matrix[y+i][i],
            matrix[y+i+1][i+1],
            matrix[y+i+2][i+2],
            matrix[y+i+3][i+3],
            matrix[y+i+4][i+4],
            matrix[y+i+5][i+5]] == SOLUTION:
            count += 1
            print(f"digonal, x={i}, y={y+i}")

for x in range(WIDTH - 6):
    for i in range(max(HEIGHT, WIDTH) - 6 - x):
        if [matrix[i][x+i],
            matrix[i+1][x+i+1],
            matrix[i+2][x+i+2],
            matrix[i+3][x+i+3],
            matrix[i+4][x+i+4],
            matrix[i+5][x+i+5]] == SOLUTION:
            count += 1
            print(f"digonal, x={x+i}, y={i}")

# print count
print(count)



