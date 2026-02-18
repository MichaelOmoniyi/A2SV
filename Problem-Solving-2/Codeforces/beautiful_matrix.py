matrix = [list(map(int, input().split())) for _ in range(5)]

count = 0
for row in range(5):
    for col in range(5):
        if matrix[row][col] == 1:
            count = abs(2-row) + abs(2-col)
            break
    if count > 0:
        break
print(count)