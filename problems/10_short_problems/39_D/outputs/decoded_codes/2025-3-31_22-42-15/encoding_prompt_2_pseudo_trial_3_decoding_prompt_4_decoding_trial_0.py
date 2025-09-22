def main():
    # Step 2: Obtain input values from the user
    firstInput = input()
    secondInput = input()

    # Step 4 and 5: Split the input strings into lists
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Step 6: Initialize the discrepancy count
    discrepancyCount = 0

    # Step 7: Loop through the first three indices
    for i in range(3):
        # Convert values to integers
        valueFromFirst = int(firstValues[i])
        valueFromSecond = int(secondValues[i])
        
        # Compare values and count discrepancies
        if valueFromFirst != valueFromSecond:
            discrepancyCount += 1

    # Step 8: Output the result based on discrepancy count
    if discrepancyCount < 3:
        print("YES")
    else:
        print("NO")

# End the main process
if __name__ == "__main__":
    main()
