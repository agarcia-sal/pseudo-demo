# Start Program

# Receive Input
firstSet = input()
secondSet = input()

# Process Input
firstSet = firstSet.split()
secondSet = secondSet.split()

# Initialize Difference Counter
differenceCount = 0

# Compare Values
for i in range(3):  # Loop through indices 0 to 2
    firstValue = int(firstSet[i])
    secondValue = int(secondSet[i])
    if firstValue != secondValue:
        differenceCount += 1

# Determine Result
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End Program
