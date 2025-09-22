# Start the program

# Read input
firstLine = input()
secondLine = input()

# Split the input
firstList = firstLine.split()
secondList = secondLine.split()

# Initialize a variable
differenceCount = 0

# Compare elements
for i in range(3):  # Loop for the first three elements
    firstValue = int(firstList[i])  # Convert to integer
    secondValue = int(secondList[i])  # Convert to integer
    
    if firstValue != secondValue:  # Check for inequality
        differenceCount += 1  # Increase the counter

# Evaluate the result
if differenceCount < 3:
    print("YES")  # Output if differences are less than 3
else:
    print("NO")  # Output if differences are 3 or more

# End the program
