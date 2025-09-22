def doMain():
    # Get input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input into components
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable for mismatches
    mismatchCount = 0
    
    # Compare corresponding elements
    for index in range(3):  # Looping from 0 to 2 inclusive
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        if firstValue != secondValue:
            mismatchCount += 1
            
    # Decide output based on mismatches
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
if __name__ == "__main__":
    doMain()
