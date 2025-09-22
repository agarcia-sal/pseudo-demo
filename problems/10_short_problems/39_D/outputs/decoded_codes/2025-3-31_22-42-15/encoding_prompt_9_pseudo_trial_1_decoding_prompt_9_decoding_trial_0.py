# Start Program

# Receive Input
firstSet = input()
secondSet = input()

# Split Input into Individual Numbers
firstNumbers = firstSet.split()
secondNumbers = secondSet.split()

# Initialize Difference Count
differenceCount = 0

# Compare the Numbers
for i in range(3):  # Iterate for each of the three numbers
    firstNumber = int(firstNumbers[i])  # Convert to integer
    secondNumber = int(secondNumbers[i])  # Convert to integer
    if firstNumber != secondNumber:  # Check if they differ
        differenceCount += 1  # Increment the difference count if they differ

# Evaluate Differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End Program
