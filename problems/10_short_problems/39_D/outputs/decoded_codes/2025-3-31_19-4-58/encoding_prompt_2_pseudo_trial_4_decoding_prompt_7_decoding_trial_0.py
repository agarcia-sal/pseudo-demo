def doMain():
    # 1. Input Handling
    inputFirstLine = input()  # Read the first line of input
    inputSecondLine = input()  # Read the second line of input
    firstList = inputFirstLine.split()  # Split input into a list of strings
    secondList = inputSecondLine.split()  # Split input into a list of strings

    # 2. Initialize a Counter
    differenceCount = 0  # This will count the differing elements

    # 3. Comparison Loop
    for index in range(3):  # Loop through the first three elements (indices 0 to 2)
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        if firstValue != secondValue:  # Check if the values are different
            differenceCount += 1  # Increment the count if they differ

    # 4. Output Decision
    if differenceCount < 3:  # If fewer than 3 differences
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO"

# 5. Function Invocation
doMain()  # Execute the function
