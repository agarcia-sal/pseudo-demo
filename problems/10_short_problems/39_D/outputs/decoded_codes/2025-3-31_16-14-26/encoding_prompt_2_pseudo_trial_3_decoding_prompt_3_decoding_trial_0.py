def doMain():
    # Prompt user for the first set of values and store them
    firstInput = input()
    # Prompt user for the second set of values and store them
    secondInput = input()
    
    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through three iterations
    for i in range(3):
        # Convert string values to integers
        firstValue = int(firstValues[i])
        secondValue = int(secondValues[i])
        
        # Compare the values and update the difference count if they differ
        if firstValue != secondValue:
            differenceCount += 1
            
    # Check the final count of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the function if this script is run directly
if __name__ == "__main__":
    doMain()
