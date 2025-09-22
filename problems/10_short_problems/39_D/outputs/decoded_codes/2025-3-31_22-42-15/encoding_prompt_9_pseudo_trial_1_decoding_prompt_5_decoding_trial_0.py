# Start Program

# Receive Input
firstSet = input()  # Read the first set of three numbers
secondSet = input()  # Read the second set of three numbers

# Split Input into Individual Numbers
firstNumbers = firstSet.split()  # Split firstSet into a list of individual numbers
secondNumbers = secondSet.split()  # Split secondSet into a list of individual numbers

# Initialize Difference Count
differenceCount = 0  # Set difference count to zero

# Compare the Numbers
for i in range(3):  # For each position from 0 to 2
    firstNumber = int(firstNumbers[i])  # Convert the number at position i in firstNumbers to integer
    secondNumber = int(secondNumbers[i])  # Convert the number at position i in secondNumbers to integer
    if firstNumber != secondNumber:  # If the numbers are not equal
        differenceCount += 1  # Increment difference count by 1

# Evaluate Differences
if differenceCount < 3:  # If differences are less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Otherwise, output "NO"

# End Program
