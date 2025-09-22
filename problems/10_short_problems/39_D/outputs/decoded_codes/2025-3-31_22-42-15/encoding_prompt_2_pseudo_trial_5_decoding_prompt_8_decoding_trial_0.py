def doMain():
    firstInput = input()
    secondInput = input()

    firstList = firstInput.split()
    secondList = secondInput.split()

    mismatchCount = 0

    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        if firstValue != secondValue:
            mismatchCount += 1

    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
