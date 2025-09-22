def main():
    # Receive Input
    firstInput = input()
    secondInput = input()

    # Process Input
    firstValues = firstInput.split()
    secondValues = secondInput.split()

    # Initialize discrepancy count
    discrepancyCount = 0

    # Comparison Loop
    for index in range(3):  # Loop through the first three elements
        valueFromFirst = int(firstValues[index])
        valueFromSecond = int(secondValues[index])
        
        # Check for discrepancies
        if valueFromFirst != valueFromSecond:
            discrepancyCount += 1

    # Final Decision
    if discrepancyCount < 3:
        print("YES")
    else:
        print("NO")

# Start the main procedure
if __name__ == "__main__":
    main()
