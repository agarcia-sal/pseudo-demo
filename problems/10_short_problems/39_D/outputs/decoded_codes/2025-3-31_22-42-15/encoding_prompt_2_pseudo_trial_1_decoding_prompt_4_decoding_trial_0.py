def main():
    # Prompt user for the first set of values
    firstInput = input()
    # Prompt user for the second set of values
    secondInput = input()
    
    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for the differences
    differenceCount = 0
    
    # Loop through the first three indices (0 to 2)
    for index in range(3):
        # Convert values to integers
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Increment the difference count if values differ
        if firstValue != secondValue:
            differenceCount += 1
    
    # Check the count of differences and output result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
