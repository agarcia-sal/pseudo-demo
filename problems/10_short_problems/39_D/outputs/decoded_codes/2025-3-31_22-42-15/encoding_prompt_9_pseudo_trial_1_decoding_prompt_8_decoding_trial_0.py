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
for i in range(3):
    firstNumber = int(firstNumbers[i])
    secondNumber = int(secondNumbers[i])
    if firstNumber != secondNumber:
        differenceCount += 1

# Evaluate Differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End Program


    def compare_sets(firstSet, secondSet):
        firstNumbers = firstSet.split()
        secondNumbers = secondSet.split()
        differenceCount = sum(1 for i in range(len(firstNumbers)) if firstNumbers[i] != secondNumbers[i])
        return "YES" if differenceCount < 3 else "NO"
    