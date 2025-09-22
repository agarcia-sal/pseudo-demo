def main():
    # Get inputs from the user
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of strings
    firstSet = firstInput.split()
    secondSet = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Compare each corresponding number in both sets
    for index in range(3):  # Looping through three positions (0, 1, 2)
        # Convert string numbers to integers
        firstNumber = int(firstSet[index])
        secondNumber = int(secondSet[index])

        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1  # Increment the difference count if they are not equal

    # Determine if the count of differences is less than 3
    if differenceCount < 3:
        print("YES")  # Print YES if differences are less than three
    else:
        print("NO")   # Otherwise, print NO

# Start the program
main()
