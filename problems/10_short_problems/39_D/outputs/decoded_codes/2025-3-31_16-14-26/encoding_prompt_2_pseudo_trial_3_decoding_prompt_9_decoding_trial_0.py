def doMain():
    # Prompt the user for input values
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of values
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize a counter for the number of differing values
    differenceCount = 0
    
    # Loop through the first and second values for three iterations
    for index in range(3):
        firstValue = int(firstValues[index])  # Convert the current value from firstValues to an integer
        secondValue = int(secondValues[index])  # Convert the current value from secondValues to an integer
        
        # Compare the two values and count differences
        if firstValue != secondValue:
            differenceCount += 1
    
    # Check the total number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# If the script is run as the main program, execute doMain
if __name__ == "__main__":
    doMain()
