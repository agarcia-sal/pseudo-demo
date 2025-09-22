def doMain():
    firstLine = input()
    secondLine = input()

    firstList = firstLine.split()
    secondList = secondLine.split()

    differenceCount = 0

    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        if firstValue != secondValue:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
