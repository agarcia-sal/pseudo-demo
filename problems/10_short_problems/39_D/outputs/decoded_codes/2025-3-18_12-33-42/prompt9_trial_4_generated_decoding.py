# Start Program

# Receive Input
firstSet = input()
secondSet = input()

# Split Input into Individual Numbers
firstNumbers = firstSet.split()
secondNumbers = secondSet.split()

# Initialize a Count for Differences
differenceCount = 0

# Compare Corresponding Numbers
for index in range(3):  # We expect exactly 3 numbers in each set
    numberFromFirst = int(firstNumbers[index])  # Convert to integer
    numberFromSecond = int(secondNumbers[index])  # Convert to integer
    if numberFromFirst != numberFromSecond:
        differenceCount += 1  # Increment the count of differences

# Determine Output Based on Differences
if differenceCount < 3:
    print("YES")
else:
    print("NO")

# End Program
