# Start Program

# Receive Input
firstSet = input()
secondSet = input()

# Process Input
firstValues = firstSet.split()
secondValues = secondSet.split()

# Initialize Difference Counter
differenceCount = 0

# Compare Values
for i in range(3):  # Loop through indices 0 to 2 inclusive
    firstValue = int(firstValues[i])  # Convert to integer
    secondValue = int(secondValues[i])  # Convert to integer
    if firstValue != secondValue:
        differenceCount += 1  # Increment if values are different

# Determine Result
if differenceCount < 3:
    print("YES")  # Indicate sets differ in fewer than three positions
else:
    print("NO")  # Indicate sets differ in three or more positions

# End Program
