import math

n = int(input())
bananas = [list(map(int, input().split(" "))) for _ in range(n)]

for banana in bananas:
    maxVal = 1
    firstVal = min(banana) + 3
    banana.remove(min(banana))
    if firstVal < min(banana):
        firstVal += 2
        maxVal *= (firstVal * math.prod(banana))
    else:
        secondVal = min(banana) + 2
        banana.remove(min(firstVal, min(banana)))
        maxVal *= (firstVal * secondVal * math.prod(banana))
    
    print(maxVal)