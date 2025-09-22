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
for index in range(3):  # Looping through indices 0 to 2
    firstNumber = int(firstList[index])
    secondNumber = int(secondList[index])
    if firstNumber != secondNumber:  # Check for differences
        differenceCount += 1  # Increase count if numbers differ

# Determine the Result
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End the Program
