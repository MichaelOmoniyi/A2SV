matrix = [list(map(int, input().split())) for _ in range(5)]

count = 0
center = len(matrix) // 2
for row in range(5):
    for col in range(5):
        if matrix[row][col] == 1:
            count = abs(center-row) + abs(center-col)
            break
    if count > 0:
        break
print(count)