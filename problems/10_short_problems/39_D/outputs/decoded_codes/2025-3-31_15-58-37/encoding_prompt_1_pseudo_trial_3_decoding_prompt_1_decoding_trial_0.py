def doMain():
    # Input Handling
    firstInput = input()
    secondInput = input()
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize Counter
    differenceCount = 0

    # Comparison Loop
    for i in range(3):  # Loop through indices 0 to 2
        valueA = int(firstList[i])         # Convert to integer
        valueB = int(secondList[i])        # Convert to integer
        if valueA != valueB:               # Check for differences
            differenceCount += 1            # Increment counter

    # Decision Making
    if differenceCount < 3:                # Check the count of differences
        print("YES")
    else:
        print("NO")

# Execution Block
if __name__ == "__main__":
    doMain()
