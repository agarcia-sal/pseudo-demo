n = int(input())
isTrue = [True] * n
currentIndex = 0
step = 1

while step <= 500000:
    if isTrue[currentIndex]:
        isTrue[currentIndex] = False
    step += 1
    currentIndex = (currentIndex + step) % n

remainingTrue = [value for value in isTrue if value]

if len(remainingTrue) == 0:
    print("YES")
else:
    print("NO")
