# 1. Start the program.

# 2. Define the main function: `doMain`.
def doMain():
    # 3. Get user input:
    firstInput = input()
    secondInput = input()

    # 4. Split the inputs into lists:
    firstList = firstInput.split()
    secondList = secondInput.split()

    # 5. Initialize a counter:
    differenceCount = 0

    # 6. Compare corresponding elements from the two lists:
    for i in range(3):  # For each index from 0 to 2 (inclusive)
        firstValue = int(firstList[i])  # Convert to integer
        secondValue = int(secondList[i])  # Convert to integer
        if firstValue != secondValue:  # If values differ
            differenceCount += 1  # Increase the counter

    # 7. Determine the result based on the count of differences:
    if differenceCount < 3:  # If differenceCount is less than 3
        print("YES")  # Print "YES"
    else:
        print("NO")  # Otherwise, print "NO"

# 8. Execute the main function if the program is run as the main module.
if __name__ == "__main__":
    doMain()

# 9. End the program.
