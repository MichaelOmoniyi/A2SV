n, k = input().split()

sequence = []
numberFound = False

for i in range(1, int(n) + 1, 2):
    sequence.append(i)
    if len(sequence) >= int(k):
        print(sequence[int(k) - 1])
        numberFound = True
        break

if numberFound == False:
    for j in range(2, int(n) + 1, 2):
        sequence.append(j)
        if len(sequence) >= int(k):
            print(sequence[int(k) - 1])
            break