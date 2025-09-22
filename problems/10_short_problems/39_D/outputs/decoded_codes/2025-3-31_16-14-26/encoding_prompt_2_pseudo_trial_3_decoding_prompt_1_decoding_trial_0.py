def doMain():
    # Prompt the user for input
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()
    
    # Initialize the difference count
    differenceCount = 0
    
    # Loop for three iterations
    for i in range(3):
        firstValue = int(firstValues[i])
        secondValue = int(secondValues[i])

        # Compare the values and count differences
        if firstValue != secondValue:
            differenceCount += 1
            
    # Check the final count of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Check if the program is executed as the main program
if __name__ == "__main__":
    doMain()
