n = int(input())
friends = list(map(int, input().split(" ")))
giftMap = {}
giftList = []

for friend in range(len(friends)):
    giftMap[friends[friend]] = friend + 1

for i in range(1, len(friends) + 1):
    print(giftMap[i], end=" ")