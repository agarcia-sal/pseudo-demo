def doMain():
    firstInput = input()
    secondInput = input()
    
    firstNumbers = firstInput.split()
    secondNumbers = secondInput.split()
    
    differenceCount = 0
    
    for i in range(3):
        firstValue = int(firstNumbers[i])
        secondValue = int(secondNumbers[i])
        
        if firstValue != secondValue:
            differenceCount += 1
            
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")
        
doMain()
