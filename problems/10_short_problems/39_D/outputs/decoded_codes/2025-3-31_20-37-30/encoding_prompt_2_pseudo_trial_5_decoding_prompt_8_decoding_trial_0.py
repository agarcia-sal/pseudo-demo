def main():
    firstInput = input()
    secondInput = input()
    
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    differenceCount = 0
    
    for i in range(3):
        firstValue = int(firstList[i])
        secondValue = int(secondList[i])
        
        if firstValue != secondValue:
            differenceCount += 1

    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
