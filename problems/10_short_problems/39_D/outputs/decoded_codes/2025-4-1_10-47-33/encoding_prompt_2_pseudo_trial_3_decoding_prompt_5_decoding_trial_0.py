def main():
    # Prompt for user input
    firstInput = input()
    secondInput = input()

    # Process the inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0

    # Compare elements of both lists
    for index in range(3):  # Loop through first three elements
        # Convert to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Increment counter if values differ
        if firstValue != secondValue:
            differenceCount += 1

    # Decide the result based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# If this file is executed as the main program, call the main function
if __name__ == "__main__":
    main()
