matrix = [list(map(int, input().split())) for _ in range(5)]

count = 0
for row in range(5):
    for col in range(5):
        if matrix[row][col] == 1:
            count += abs(row-col)
            break
    if count > 0:
        break
print(count)