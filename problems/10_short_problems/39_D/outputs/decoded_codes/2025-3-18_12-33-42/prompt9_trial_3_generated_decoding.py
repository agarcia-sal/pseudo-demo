def doMain():
    # Read input from the user for the first and second list
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of components
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for the differences
    differenceCount = 0

    # Compare corresponding elements from both lists
    for i in range(3):  # Assuming the lists have exactly 3 elements
        firstNumber = int(firstList[i])  # Convert to integer
        secondNumber = int(secondList[i])  # Convert to integer
        
        # Check if the numbers differ
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment the difference counter

    # Determine if the differences are fewer than 3
    if differenceCount < 3:
        print("YES")  # Output YES if differences are fewer than 3
    else:
        print("NO")   # Output NO otherwise

# Execute the main process if the script is run directly
if __name__ == "__main__":
    doMain()
