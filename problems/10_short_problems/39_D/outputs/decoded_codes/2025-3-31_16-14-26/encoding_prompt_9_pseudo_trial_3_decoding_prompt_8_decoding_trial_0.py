def doMain():
    firstSequence = input().split()
    secondSequence = input().split()
    differenceCount = 0

    for i in range(3):
        firstValue = int(firstSequence[i])
        secondValue = int(secondSequence[i])
        if firstValue != secondValue:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

doMain()
