def doMain():
    # Input Handling: Get User Input
    firstInput = input()
    secondInput = input()
    
    # Data Processing: Split Inputs into Lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Comparison Logic: Count Differences
    differenceCount = 0
    for i in range(3):  # Repeat for each of the first three elements
        numberFromFirstList = int(firstList[i])
        numberFromSecondList = int(secondList[i])
        if numberFromFirstList != numberFromSecondList:
            differenceCount += 1
            
    # Final Decision: Output Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Program Execution: Start the Main Function
if __name__ == "__main__":
    doMain()
