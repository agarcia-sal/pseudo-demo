def main():
    # Input Phase
    firstSequence = input()
    secondSequence = input()
    
    # Process Input
    firstList = firstSequence.split()
    secondList = secondSequence.split()
    
    # Initialize Difference Counter
    differenceCount = 0
    
    # Comparison Loop
    for i in range(3):
        numberFromFirst = int(firstList[i])
        numberFromSecond = int(secondList[i])
        if numberFromFirst != numberFromSecond:
            differenceCount += 1

    # Decision-making
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execution context
if __name__ == "__main__":
    main()
