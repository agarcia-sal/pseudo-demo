def main():
    # Receive Input
    firstInput = input()
    secondInput = input()

    # Process Input
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize a count variable
    discrepancyCount = 0

    # Comparison Loop
    for index in range(3):
        valueFromFirst = int(firstValues[index])
        valueFromSecond = int(secondValues[index])
        if valueFromFirst != valueFromSecond:
            discrepancyCount += 1

    # Final Decision
    if discrepancyCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main procedure
main()
