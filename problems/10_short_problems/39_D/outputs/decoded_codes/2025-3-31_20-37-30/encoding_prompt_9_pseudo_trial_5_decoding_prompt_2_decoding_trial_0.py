# Start the program.

# Receive Input:
firstSet = input()
secondSet = input()

# Process Input:
firstNumbers = firstSet.split()
secondNumbers = secondSet.split()

# Initialize Differences Counter:
differenceCount = 0

# Compare Numbers:
for index in range(3):  # Loop through the indices 0, 1, 2
    firstNumber = int(firstNumbers[index])  # Convert to integer
    secondNumber = int(secondNumbers[index])  # Convert to integer
    
    if firstNumber != secondNumber:
        differenceCount += 1  # Increase counter if numbers differ

# Determine Output:
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End the program.
