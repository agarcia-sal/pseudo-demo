# Start the Program

# Receive Input
firstInput = input()
secondInput = input()

# Split Input into Individual Numbers
firstNumbers = firstInput.split()
secondNumbers = secondInput.split()

# Initialize Difference Counter
differenceCount = 0

# Compare Corresponding Numbers
for index in range(3):  # Loop through indices 0, 1, 2
    numberFromFirst = int(firstNumbers[index])  # Convert to integer
    numberFromSecond = int(secondNumbers[index])  # Convert to integer
    if numberFromFirst != numberFromSecond:  # Check for differences
        differenceCount += 1  # Increment counter if numbers differ

# Evaluate the Difference Count
if differenceCount < 3:
    print("YES")  # Output YES if differences are fewer than 3
else:
    print("NO")   # Output NO if differences are 3 or more

# End the Program
