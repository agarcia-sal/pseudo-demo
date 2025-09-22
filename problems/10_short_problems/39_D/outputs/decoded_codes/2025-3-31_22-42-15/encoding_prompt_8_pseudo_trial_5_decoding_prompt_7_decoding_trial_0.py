def main():
    # Read two lines of input from the user, each representing a set of integers
    firstInput = input()
    secondInput = input()

    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter to keep track of differences
    differenceCount = 0 

    # Loop through each index from 0 to 2 (representing the three integers)
    for index in range(3):
        # Convert the string representations to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 

    # Determine whether the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
