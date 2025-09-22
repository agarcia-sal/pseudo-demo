# Start the program

# Receive input
firstInput = input()  # Read the first line of input
secondInput = input()  # Read the second line of input

# Process the inputs
firstList = firstInput.split()  # Split 'firstInput' into a list of strings
secondList = secondInput.split()  # Split 'secondInput' into a list of strings
differenceCount = 0  # Initialize a variable to track the number of differing elements

# Compare elements
for index in range(3):  # Iterate over the first three indices
    firstNumber = int(firstList[index])  # Convert to integer
    secondNumber = int(secondList[index])  # Convert to integer
    if firstNumber != secondNumber:  # Check if the numbers differ
        differenceCount += 1  # Increment difference count if they are not equal

# Evaluate the results
if differenceCount < 3:  # Check if the difference count is less than 3
    print("YES")  # Output "YES" if condition is met
else:
    print("NO")  # Output "NO" if condition isn't met

# End the program
