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
for i in range(3):  # Loop through positions 0 to 2
    firstNumber = int(firstNumbers[i])  # Convert to integer
    secondNumber = int(secondNumbers[i])  # Convert to integer
    if firstNumber != secondNumber:  # Compare the numbers
        differenceCount += 1  # Increment difference count

# Evaluate Differences
if differenceCount < 3:
    print("YES")  # Less than 3 differences
else:
    print("NO")  # 3 or more differences

# End Program
