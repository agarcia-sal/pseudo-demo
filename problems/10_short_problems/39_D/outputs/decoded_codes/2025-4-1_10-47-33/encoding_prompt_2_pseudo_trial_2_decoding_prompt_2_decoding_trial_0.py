# Start the program.

# Receive input:
firstInput = input()
secondInput = input()

# Process the inputs:
firstList = firstInput.split()
secondList = secondInput.split()
differenceCount = 0  # Initialize variable to track differing elements

# Compare elements:
for index in range(3):  # Loop from 0 to 2
    firstNumber = int(firstList[index])      # Convert to integer
    secondNumber = int(secondList[index])    # Convert to integer
    if firstNumber != secondNumber:           # Check for difference
        differenceCount += 1                   # Increment count if different

# Evaluate the results:
if differenceCount < 3:                       # Check difference count
    print("YES")                              # Output YES if condition met
else:
    print("NO")                               # Output NO otherwise

# End the program.
