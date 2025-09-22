def compareInputValues():
    firstInput = input()
    secondInput = input()
    
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    mismatchCount = 0
    
    for index in range(3):
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        if firstValue != secondValue:
            mismatchCount += 1
            
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    compareInputValues()
