def compareThreeInputs():
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    differenceCount = 0 
    
    for index in range(3):
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])
        
        if firstNumber != secondNumber:
            differenceCount += 1
            
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    compareThreeInputs()
