# Start the Program

# Receive Input
firstSet = input().split()
secondSet = input().split()

# Initialize a Difference Counter
differenceCount = 0

# Compare Corresponding Numbers
for i in range(3):
    firstNumber = int(firstSet[i])
    secondNumber = int(secondSet[i])
    if firstNumber != secondNumber:
        differenceCount += 1

# Check the Number of Differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End of Program
