def main():
    firstList = input()
    secondList = input()
    
    firstValues = firstList.split()
    secondValues = secondList.split()
    
    differenceCount = 0
    
    for x in range(3):
        valueA = int(firstValues[x])
        valueB = int(secondValues[x])
        
        if valueA != valueB:
            differenceCount += 1
    
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
