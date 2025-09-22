# Start Program

# Receive Input
firstSet = []
secondSet = []

# Read the first set of numbers
for i in range(3):
    firstSet.append(int(input()))

# Read the second set of numbers
for i in range(3):
    secondSet.append(int(input()))

# Initialize Difference Count
differenceCount = 0

# Loop through the Sets
for index in range(3):  # since there are exactly three numbers
    # Compare numbers at the current index
    if firstSet[index] != secondSet[index]:
        differenceCount += 1  # Increase difference count if numbers differ

# Check the Number of Differences
if differenceCount < 3:
    print("YES")  # Fewer than three differences
else:
    print("NO")   # Three or more differences

# End Program
