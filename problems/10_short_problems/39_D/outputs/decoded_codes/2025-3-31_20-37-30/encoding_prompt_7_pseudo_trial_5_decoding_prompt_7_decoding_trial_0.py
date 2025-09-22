def main():
    # Read two lines of input representing two sets of three values
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three values to compare both sets
    for index in range(3):
        # Convert the values from string to integer for comparison
        firstValue = int(firstValues[index])
        secondValue = int(secondValues[index])
        
        # Check if the current values are different
        if firstValue != secondValue:
            # Increment the difference count if they are not the same
            differenceCount += 1
            
    # Determine the output based on the number of differences found
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is being run as the main program
if __name__ == "__main__":
    main()
