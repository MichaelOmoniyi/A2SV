n = int(input())
bananas = [list(map(int, input().split(" "))) for _ in range(n)]

for banana in bananas:
    for i in range(5):
        banana.sort()
        banana[0] += 1

    print(banana[0] * banana[1] * banana[2])