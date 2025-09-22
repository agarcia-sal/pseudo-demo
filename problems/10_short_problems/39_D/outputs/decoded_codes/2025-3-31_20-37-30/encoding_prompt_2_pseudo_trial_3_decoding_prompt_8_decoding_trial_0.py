def doMain():
    firstInputString = input()
    secondInputString = input()
    
    firstInputList = firstInputString.split()
    secondInputList = secondInputString.split()
    
    differenceCount = 0
    
    for index in range(3):
        firstValue = int(firstInputList[index])
        secondValue = int(secondInputList[index])
        if firstValue != secondValue:
            differenceCount += 1
            
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    doMain()
