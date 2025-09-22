# Start Program

# Step 2: Receive Input
firstSet = []
secondSet = []

# Read the first set of numbers from the user
for _ in range(3):
    number = int(input())
    firstSet.append(number)

# Read the second set of numbers from the user
for _ in range(3):
    number = int(input())
    secondSet.append(number)

# Step 3: Initialize Difference Count
differenceCount = 0

# Step 4: Loop through the Sets
for i in range(3):
    if firstSet[i] != secondSet[i]:
        differenceCount += 1

# Step 5: Check the Number of Differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End Program
