# Start Program

# Receive Input:
firstSet = input()  # Read the first line of input
secondSet = input()  # Read the second line of input

# Process Input:
firstSet = firstSet.split()  # Split firstSet into individual values
secondSet = secondSet.split()  # Split secondSet into individual values

# Initialize Difference Counter:
differenceCount = 0  # To keep track of how many values differ

# Compare Values:
for index in range(3):  # For each index from 0 to 2 (inclusive)
    firstValue = int(firstSet[index])  # Convert firstSet value to a number
    secondValue = int(secondSet[index])  # Convert secondSet value to a number
    if firstValue != secondValue:  # If the values are not equal
        differenceCount += 1  # Increment the difference count

# Determine Result:
if differenceCount < 3:  # If fewer than 3 differences
    print("YES")  # Output "YES"
else:  # If 3 or more differences
    print("NO")  # Output "NO"

# End Program
