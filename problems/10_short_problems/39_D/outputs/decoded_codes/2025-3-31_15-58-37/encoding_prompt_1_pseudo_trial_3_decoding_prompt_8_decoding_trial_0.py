def doMain():
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()

    differenceCount = 0
    
    for index in range(3):
        valueA = int(firstList[index])
        valueB = int(secondList[index])
        if valueA != valueB:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
