# Start the program

# Receive input
firstInput = input()  # Read the first line of input
secondInput = input()  # Read the second line of input

# Process the inputs
firstList = firstInput.split()  # Split first input into a list of strings
secondList = secondInput.split()  # Split second input into a list of strings
differenceCount = 0  # Initialize a variable to track the number of differing elements

# Compare elements
for index in range(3):  # Loop over the first three indices
    firstNumber = int(firstList[index])  # Convert to integer from first list
    secondNumber = int(secondList[index])  # Convert to integer from second list
    if firstNumber != secondNumber:  # Check if they are different
        differenceCount += 1  # Increment count if they are different

# Evaluate the results
if differenceCount < 3:  # If differences are less than 3
    print("YES")  # Output "YES"
else:  # Otherwise
    print("NO")  # Output "NO"

# End the program
