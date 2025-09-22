# Start the program

# Receive input
firstInput = input()
secondInput = input()

# Process the inputs
firstList = firstInput.split()
secondList = secondInput.split()
differenceCount = 0  # Initialize a variable to track differing elements

# Compare elements
for index in range(3):  # Loop through indices 0 to 2
    firstNumber = int(firstList[index])  # Convert current element of firstList to integer
    secondNumber = int(secondList[index])  # Convert current element of secondList to integer
    if firstNumber != secondNumber:  # If the numbers do not match
        differenceCount += 1  # Increment the difference count

# Evaluate the results
if differenceCount < 3:  # If differences are less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise output "NO"

# End the program
