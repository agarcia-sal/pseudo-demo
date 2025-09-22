def main():
    # Read two lines of input from the user
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a variable to count differences
    differenceCount = 0

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are not equal
        if firstValue != secondValue:
            # Increment the difference count
            differenceCount += 1

    # Check the number of differences counted
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this file is run as a program
if __name__ == "__main__":
    main()
