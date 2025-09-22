numberOfElements = int(input())
isActive = [True] * numberOfElements
index = 0
step = 1

while step <= 500000:
    if isActive[index]:
        isActive[index] = False
    step += 1
    index = (index + step) % numberOfElements

activeElements = [elem for elem in isActive if elem]

if len(activeElements) == 0:
    print('YES')
else:
    print('NO')
