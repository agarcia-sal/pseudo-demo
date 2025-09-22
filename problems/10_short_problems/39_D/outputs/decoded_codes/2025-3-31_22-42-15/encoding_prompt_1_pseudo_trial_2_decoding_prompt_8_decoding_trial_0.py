def doMain():
    firstInput = input()
    secondInput = input()
    
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    differenceCount = 0

    for index in range(3):
        valueA = int(firstValues[index])
        valueB = int(secondValues[index])
        if valueA != valueB:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
