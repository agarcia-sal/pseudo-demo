def main():
    # Step 2: Receive Input
    firstInput = input()
    secondInput = input()

    # Step 3: Process Input
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Step 4: Initialize a count variable
    discrepancyCount = 0

    # Step 5: Comparison Loop
    for index in range(3):  # We check the first three elements
        valueFromFirst = int(firstValues[index])
        valueFromSecond = int(secondValues[index])

        # Check if the values are not equal
        if valueFromFirst != valueFromSecond:
            discrepancyCount += 1

    # Step 6: Final Decision
    if discrepancyCount < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
main()
