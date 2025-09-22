def main():
    # Step 2: Obtain the first set of input values from the user
    firstInput = input()

    # Step 3: Obtain the second set of input values from the user
    secondInput = input()

    # Step 4: Split the inputs into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Step 6: Initialize discrepancy count
    discrepancyCount = 0

    # Step 7: Compare the first three values from both inputs
    for index in range(3):
        valueFromFirst = int(firstValues[index])
        valueFromSecond = int(secondValues[index])

        # Compare the values
        if valueFromFirst != valueFromSecond:
            discrepancyCount += 1

    # Step 8: Evaluate the discrepancy count
    if discrepancyCount < 3:
        print("YES")
    else:
        print("NO")

# Step 9: Call the main function to run the program
if __name__ == "__main__":
    main()
