def doMain():
    firstInput = input()
    secondInput = input()
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    differenceCount = 0

    for i in range(3):
        firstValue = int(firstValues[i])
        secondValue = int(secondValues[i])
        if firstValue != secondValue:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
