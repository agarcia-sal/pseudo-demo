def main():
    # Step 1: Gather user input
    firstSet = input()
    secondSet = input()

    # Step 2: Split the input strings into individual numbers
    firstNumbers = firstSet.split()
    secondNumbers = secondSet.split()

    # Step 3: Initialize a counter for differences
    differenceCount = 0

    # Step 4: Compare each number in the two sets
    for index in range(3):  # Assuming we are always comparing exactly three numbers
        # Convert the current numbers from string to integer
        numberFromFirstSet = int(firstNumbers[index])
        numberFromSecondSet = int(secondNumbers[index])

        # Check if the numbers are different
        if numberFromFirstSet != numberFromSecondSet:
            # Increment the count of differences
            differenceCount += 1

    # Step 5: Determine the output based on the count of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Entry point of the program
main()
