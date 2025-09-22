def main():
    # Read input from the user
    firstInput = input()
    secondInput = input()

    # Split input strings into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Check the first three elements of both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Compare elements and count differences
        if firstValue != secondValue:
            differenceCount += 1

    # Determine result based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
