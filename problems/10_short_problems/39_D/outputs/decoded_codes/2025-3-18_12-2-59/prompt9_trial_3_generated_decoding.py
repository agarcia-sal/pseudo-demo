# Start the Program

# Receive Input
firstSet = input()  # Receive the first set of three numbers
secondSet = input()  # Receive the second set of three numbers

# Split Input
firstNumbers = firstSet.split()  # Split the input string into a list
secondNumbers = secondSet.split()  # Split the second input string into a list

# Initialize Difference Counter
differenceCount = 0  # Set starting count of differences to 0

# Compare Numbers
for index in range(3):  # Loop through the first three numbers
    # Convert to integers
    firstNumber = int(firstNumbers[index])  # Convert current number from the first set
    secondNumber = int(secondNumbers[index])  # Convert current number from the second set
    
    # Check for differences
    if firstNumber != secondNumber:  # If numbers at the same index are not equal
        differenceCount += 1  # Increment the difference count

# Determine Output
if differenceCount < 3:  # If differences are less than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End the Program
