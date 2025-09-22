def doMain():
    # Accept input for both sets of values
    firstInput = input()
    secondInput = input()

    # Split the input values into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize counter for differences
    differenceCount = 0

    # Compare values at each index
    for x in range(3):  # Loop from 0 to 2 (inclusive)
        firstValue = int(firstValues[x])  # Convert first value at index x to integer
        secondValue = int(secondValues[x])  # Convert second value at index x to integer
        
        # Check if values differ
        if firstValue != secondValue:
            differenceCount += 1  # Increase the counter if values are different

    # Output the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if the script is run directly
if __name__ == "__main__":
    doMain()
