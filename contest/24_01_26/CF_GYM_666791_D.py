n, k = map(int, input().split(" "))

oddCount = (n + 1) // 2

if oddCount >= k:
    print((2 * k) - 1)
else:
    print(2 * (k - oddCount))