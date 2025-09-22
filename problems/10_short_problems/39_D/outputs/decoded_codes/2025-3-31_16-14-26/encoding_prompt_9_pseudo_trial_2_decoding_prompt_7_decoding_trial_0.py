def main():
    # Step 1: Receive input
    firstSet = input()  # Prompt user for first set of three numbers
    secondSet = input()  # Prompt user for second set of three numbers

    # Step 2: Split the input strings into lists
    numbersFromFirstSet = firstSet.split()  # Split first set into a list
    numbersFromSecondSet = secondSet.split()  # Split second set into a list

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare the numbers in both sets
    for index in range(3):
        # Convert to integers for comparison
        numberFromFirst = int(numbersFromFirstSet[index])
        numberFromSecond = int(numbersFromSecondSet[index])

        # Step 5: Check if the numbers are different
        if numberFromFirst != numberFromSecond:
            # Increment difference count if they are not equal
            differenceCount += 1

    # Step 6: Evaluate the number of differences
    if differenceCount < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")  # Three or more differences

# Step 7: Execute the main function
main()
