# Purpose: To compare two sets of three integers and determine how many are different
# If fewer than three integers differ, the program outputs "YES"; otherwise, it outputs "NO"

def main():
    # Step 1: Read the first set of integers from the user
    print("Enter the first set of three integers:")
    firstSet = input()  # Reading user input for the first set

    # Step 2: Read the second set of integers from the user
    print("Enter the second set of three integers:")
    secondSet = input()  # Reading user input for the second set

    # Step 3: Split the input strings into lists of integers
    firstList = firstSet.split()  # Split the first set into individual numbers
    secondList = secondSet.split()  # Split the second set into individual numbers

    # Step 4: Initialize a counter for differences
    differenceCount = 0

    # Step 5: Compare the corresponding integers from both lists
    for index in range(3):  # Loop through the indices 0 to 2
        # Convert string to integer for comparison
        firstNumber = int(firstList[index])  # Convert to integer
        secondNumber = int(secondList[index])  # Convert to integer

        # Check if the numbers are different
        if firstNumber != secondNumber:  # If they differ
            differenceCount += 1  # Increment the counter for differences

    # Step 6: Determine the output based on the number of differences
    if differenceCount < 3:  # If fewer than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Execute the main function
main()
