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
for index in range(3):  # Loop through three positions
    firstNumber = int(firstNumbers[index])
    secondNumber = int(secondNumbers[index])
    if firstNumber != secondNumber:
        differenceCount += 1

# Determine Output
if differenceCount < 3:
    print("YES")
else:
    print("NO")
