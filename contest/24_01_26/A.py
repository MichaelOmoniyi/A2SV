n = int(input())
expressions = [list(map(int, input().split("+"))) for _ in range(n)]

for expression in expressions:
    print(sum(expression))