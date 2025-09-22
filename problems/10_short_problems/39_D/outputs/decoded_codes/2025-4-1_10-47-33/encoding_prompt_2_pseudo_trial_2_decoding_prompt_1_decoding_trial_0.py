# Start the program

# Receive input
firstInput = input()
secondInput = input()

# Process the inputs
firstList = firstInput.split()
secondList = secondInput.split()
differenceCount = 0  # Initialize differenceCount to 0

# Compare elements
for index in range(3):  # For each index from 0 to 2
    firstNumber = int(firstList[index])  # Convert element to integer
    secondNumber = int(secondList[index])  # Convert element to integer
    if firstNumber != secondNumber:  # If numbers are not equal
        differenceCount += 1  # Increment differenceCount by 1

# Evaluate the results
if differenceCount < 3:  # If differenceCount is less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End the program
