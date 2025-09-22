def doMain():
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    differenceCount = 0
    
    for i in range(min(3, len(firstList), len(secondList))):
        firstNumber = int(firstList[i])
        secondNumber = int(secondList[i])
        if firstNumber != secondNumber:
            differenceCount += 1
            
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

doMain()
