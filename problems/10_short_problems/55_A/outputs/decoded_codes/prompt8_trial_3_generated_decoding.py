n = int(input())
booleanList = [True] * n
currentIndex = 0
step = 1

while step <= 500000:
    if booleanList[currentIndex]:
        booleanList[currentIndex] = False
    step += 1
    currentIndex = (currentIndex + step) % n

remainingTrueValues = [value for value in booleanList if value]

if len(remainingTrueValues) == 0:
    print('YES')
else:
    print('NO')
