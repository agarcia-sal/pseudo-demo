# Start Main Program
firstSet = input()
secondSet = input()

# Split Input Strings
firstList = firstSet.split()
secondList = secondSet.split()

# Initialize Difference Counter
differenceCount = 0

# Check Each Position for Differences
for index in range(3):
    firstValue = int(firstList[index])
    secondValue = int(secondList[index])
    if firstValue != secondValue:
        differenceCount += 1

# Evaluate Number of Differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End Program
