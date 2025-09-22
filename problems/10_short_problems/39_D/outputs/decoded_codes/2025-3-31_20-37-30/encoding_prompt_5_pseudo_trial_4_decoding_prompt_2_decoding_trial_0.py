def doMain():
    # Accept Input
    firstInput = input()
    secondInput = input()

    # Split Input Values
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize Counter
    differenceCount = 0

    # Compare Value Pairs
    for x in range(3):  # Loop over indices 0 to 2
        firstValue = int(firstValues[x])
        secondValue = int(secondValues[x])
        if firstValue != secondValue:
            differenceCount += 1

    # Output Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute Main Function
if __name__ == "__main__":
    doMain()
