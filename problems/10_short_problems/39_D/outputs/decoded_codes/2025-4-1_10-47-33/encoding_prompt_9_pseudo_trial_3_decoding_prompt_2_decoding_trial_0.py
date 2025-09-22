def main():
    # Step 1: Read the first set of integers from the user
    print("Enter the first set of three integers:")
    firstSet = input()

    # Step 2: Read the second set of integers from the user
    print("Enter the second set of three integers:")
    secondSet = input()

    # Step 3: Split the input strings into lists of integers
    firstList = firstSet.split()
    secondList = secondSet.split()

    # Step 4: Initialize a counter for differences
    differenceCount = 0

    # Step 5: Compare the corresponding integers from both lists
    for index in range(3):
        # Convert string to integer for comparison
        firstNumber = int(firstList[index])
        secondNumber = int(secondList[index])

        # Check if the numbers are different
        if firstNumber != secondNumber:
            differenceCount += 1

    # Step 6: Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Run the main function
main()
