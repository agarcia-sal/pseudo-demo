def compareInputValues():
    # Prompt user to enter the first input string
    firstInput = input()
    # Prompt user to enter the second input string
    secondInput = input()
    
    # Split both input strings by spaces into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for mismatches
    mismatchCount = 0
    
    # Loop through the first three indices (assuming inputs are valid)
    for index in range(3):
        # Convert values to integers for comparison
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if values at the current index are different
        if firstValue != secondValue:
            mismatchCount += 1  # Increment mismatch counter if values differ
    
    # Output result based on the mismatch count
    if mismatchCount < 3:
        print("YES")  # Less than 3 mismatches
    else:
        print("NO")   # 3 or more mismatches

# Execute the function only if this script is run as the main program
if __name__ == "__main__":
    compareInputValues()
