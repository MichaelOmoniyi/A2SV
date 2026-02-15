k, n, w = input().split()
totalBananaCost = 0

for i in range(1, int(w) + 1):
    totalBananaCost += i * int(k)

if (totalBananaCost - int(n)) < 0:
    print(0)
else:
    print(totalBananaCost - int(n))