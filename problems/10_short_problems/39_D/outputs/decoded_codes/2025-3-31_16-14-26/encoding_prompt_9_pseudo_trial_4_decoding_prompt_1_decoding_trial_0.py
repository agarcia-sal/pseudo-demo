# Start the Program

# Receive Input
firstSet = input()
secondSet = input()

# Split Input into Individual Numbers
firstList = firstSet.split()
secondList = secondSet.split()

# Initialize a Counter for Differences
differenceCount = 0

# Compare Each Number in the Sets
for i in range(3):  # Looping from index 0 to 2
    firstNumber = int(firstList[i])  # Convert to integer
    secondNumber = int(secondList[i])  # Convert to integer
    if firstNumber != secondNumber:  # Compare the numbers
        differenceCount += 1  # Increase the difference count

# Determine the Result
if differenceCount < 3:
    print("YES")  # Fewer than three differences
else:
    print("NO")  # Three or more differences

# End the Program
