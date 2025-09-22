def doMain():
    # Input Handling: Read Values
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize Counter: Count Differences
    differenceCount = 0
    
    # Comparison Loop: Check Values
    for index in range(3):
        valueA = int(firstList[index])
        valueB = int(secondList[index])
        if valueA != valueB:
            differenceCount += 1
            
    # Decision Making: Output Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execution Block: Run the Main Function
if __name__ == "__main__":
    doMain()
