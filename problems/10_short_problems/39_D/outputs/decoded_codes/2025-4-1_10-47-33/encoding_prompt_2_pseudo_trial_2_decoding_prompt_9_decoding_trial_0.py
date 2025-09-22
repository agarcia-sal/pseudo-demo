# Start the program

# Receive input
firstInput = input()  # Read the first line of input
secondInput = input()  # Read the second line of input

# Process the inputs
firstList = firstInput.split()  # Split the first input string into a list of strings
secondList = secondInput.split()  # Split the second input string into a list of strings
differenceCount = 0  # Initialize a variable to track the number of differing elements

# Compare elements
for index in range(3):  # Loop over the first three indices
    firstNumber = int(firstList[index])  # Convert the current element in firstList to an integer
    secondNumber = int(secondList[index])  # Convert the current element in secondList to an integer
    
    # Check if the two numbers are different
    if firstNumber != secondNumber:
        differenceCount += 1  # Increment the difference count if they are not equal

# Evaluate the results
if differenceCount < 3:
    print("YES")  # Output "YES" if the difference count is less than 3
else:
    print("NO")  # Output "NO" if the difference count is 3 or more

# End the program
