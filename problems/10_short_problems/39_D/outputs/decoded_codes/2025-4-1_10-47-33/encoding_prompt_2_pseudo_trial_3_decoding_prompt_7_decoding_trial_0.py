def main():
    # Prompt for user input for the two lines
    firstInput = input()
    secondInput = input()

    # Process the inputs and split them into lists
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize the counter for differences
    differenceCount = 0

    # Compare the elements of both lists
    for i in range(3):  # We compare the first three elements
        firstValue = int(firstList[i])  # Convert to integer
        secondValue = int(secondList[i])  # Convert to integer
        
        # Check if the values are different
        if firstValue != secondValue:
            differenceCount += 1  # Increment the difference count

    # Decide the result based on the count of differences
    if differenceCount < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")  # Output "NO" if differences are 3 or more

# Check if the script is run as the main program and call main
if __name__ == "__main__":
    main()
