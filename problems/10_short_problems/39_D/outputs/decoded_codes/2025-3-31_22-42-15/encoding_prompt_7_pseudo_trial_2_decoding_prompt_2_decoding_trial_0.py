def compareInputValues():
    # Prompt user to enter the first input string
    firstInput = input()
    # Prompt user to enter the second input string
    secondInput = input()
    
    # Split inputs by spaces into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for mismatches
    mismatchCount = 0
    
    # Loop through the first three indices
    for index in range(3):
        # Convert string values from both lists to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check for mismatches
        if firstValue != secondValue:
            mismatchCount += 1
    
    # Conditional output based on the number of mismatches
    if mismatchCount < 3:
        print("YES")
    else:
        print("NO")

# Check if this script is run as the main program
if __name__ == "__main__":
    compareInputValues()
