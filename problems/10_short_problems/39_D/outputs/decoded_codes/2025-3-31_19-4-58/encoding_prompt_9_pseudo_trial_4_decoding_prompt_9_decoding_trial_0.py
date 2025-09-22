# Start the Program

# Receive Input
firstSet = input().split()
secondSet = input().split()

# Initialize a Difference Counter
differenceCount = 0

# Compare Corresponding Numbers
for index in range(3):  # Checking indices 0, 1, and 2
    firstNumber = int(firstSet[index])  # Convert to integer
    secondNumber = int(secondSet[index])  # Convert to integer
    if firstNumber != secondNumber:  # Check for inequality
        differenceCount += 1  # Increment difference count

# Check the Number of Differences
if differenceCount < 3:  # If differences are fewer than 3
    print("YES")
else:  # Otherwise
    print("NO")

# End of Program
