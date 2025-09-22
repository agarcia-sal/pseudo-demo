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
    firstValue = int(firstSet[i])  # Convert firstSet value to integer
    secondValue = int(secondSet[i])  # Convert secondSet value to integer
    if firstValue != secondValue:  # Check for differences
        differenceCount += 1  # Increment count if values are different

# Determine Result
if differenceCount < 3:
    print("YES")  # Output if fewer than 3 differences
else:
    print("NO")   # Output if 3 or more differences

# End Program
