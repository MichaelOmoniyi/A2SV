n = int(input())
words = [input().strip() for _ in range(n)]

for word in words:
    if len(word) <= 10:
        print(word)
    else:
        print(f"{word[0]}{len(word)-2}{word[-1]}")