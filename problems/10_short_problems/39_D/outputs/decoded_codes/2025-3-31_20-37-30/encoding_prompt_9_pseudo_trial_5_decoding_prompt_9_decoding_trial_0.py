# Start the program

# Receive Input
firstSet = input()
secondSet = input()

# Process Input
firstNumbers = firstSet.split()
secondNumbers = secondSet.split()

# Initialize Differences Counter
differenceCount = 0

# Compare Numbers
for index in range(3):  # Loop through the three indexes (0 to 2)
    firstNumber = int(firstNumbers[index])  # Convert to integer
    secondNumber = int(secondNumbers[index])  # Convert to integer
    if firstNumber != secondNumber:  # Check for differences
        differenceCount += 1  # Increment the difference count

# Determine Output
if differenceCount < 3:  # Check if differences are less than 3
    print("YES")
else:
    print("NO")

# End the program
