def main():
    # Step 2a: Read input from the user
    firstInput = input()
    secondInput = input()

    # Step 2b: Split the first input into separate elements
    firstList = firstInput.split()

    # Step 2c: Split the second input into separate elements
    secondList = secondInput.split()

    # Step 2d: Initialize a variable to count differences
    differenceCount = 0

    # Step 2e: Loop through the indices 0 to 2
    for index in range(3):
        # Convert elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Step 2e: Check if values are different
        if firstValue != secondValue:
            # Increment the count of differences
            differenceCount += 1

    # Step 2f: Check the number of differences
    if differenceCount < 3:
        # Output "YES" if differences are less than 3
        print("YES")
    else:
        # Output "NO" otherwise
        print("NO")

# Step 3: Execute the main function when the program runs
if __name__ == "__main__":
    main()
