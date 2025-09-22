# 1. Start Program

# 2. Receive Input
firstSet = input()
secondSet = input()

# 3. Process Input
firstSet = firstSet.split()
secondSet = secondSet.split()

# 4. Initialize Difference Counter
differenceCount = 0

# 5. Compare Values
for index in range(3):  # Indices 0 to 2 inclusive
    firstValue = int(firstSet[index])  # Convert to number
    secondValue = int(secondSet[index])  # Convert to number
    if firstValue != secondValue:
        differenceCount += 1

# 6. Determine Result
if differenceCount < 3:
    print("YES")  # Output if fewer than three difference positions
else:
    print("NO")   # Output if three or more different positions

# 7. End Program
