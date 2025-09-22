def main():
    # Read two lines of input
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstSet = firstInput.split()
    secondSet = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of each set
    for index in range(3):
        # Convert current elements to integers
        firstValue = int(firstSet[index])
        secondValue = int(secondSet[index])

        # Compare the two values
        if firstValue != secondValue:
            differenceCount += 1

    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()
