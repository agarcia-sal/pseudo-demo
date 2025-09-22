def doMain():
    # Input Handling: Read Values
    firstInput = input()
    secondInput = input()
    
    # Split inputs into lists
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize Counter for Counting Differences
    differenceCount = 0

    # Comparison Loop: Check Values
    for index in range(3):  # Loop through indices 0, 1, 2
        valueA = int(firstList[index])  # Convert the first list value to an integer
        valueB = int(secondList[index])  # Convert the second list value to an integer
        if valueA != valueB:  # Check for inequality
            differenceCount += 1  # Increment the counter if they are different

    # Decision Making: Output Result
    if differenceCount < 3:  # If fewer than 3 differences, print "YES"
        print("YES")
    else:  # Otherwise, print "NO"
        print("NO")

# Execution Block: Run the Main Function
if __name__ == "__main__":
    doMain()
