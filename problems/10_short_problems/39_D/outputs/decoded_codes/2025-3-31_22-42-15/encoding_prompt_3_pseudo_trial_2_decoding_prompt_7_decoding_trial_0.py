def main():
    # Step 1: Collect input from the user
    firstInput = input()  # Get first sequence of numbers
    secondInput = input()  # Get second sequence of numbers

    # Step 2: Split the input strings into separate components
    firstList = firstInput.split()  # Convert the first input into a list of strings
    secondList = secondInput.split()  # Convert the second input into a list of strings

    # Step 3: Initialize a counter for differences
    differenceCount = 0  # Counter for counting the differences

    # Step 4: Compare elements from both lists
    for index in range(3):  # Loop through the first three elements
        firstValue = int(firstList[index])  # Convert the first list element to an integer
        secondValue = int(secondList[index])  # Convert the second list element to an integer

        # Step 5: Check if the values are different
        if firstValue != secondValue:  # If values are not equal
            differenceCount += 1  # Increment the difference counter

    # Step 6: Determine the output based on the number of differences
    if differenceCount < 3:  # If the number of differences is less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Step 7: Execute the main function if this script is run
if __name__ == "__main__":
    main()  # Call the main function
