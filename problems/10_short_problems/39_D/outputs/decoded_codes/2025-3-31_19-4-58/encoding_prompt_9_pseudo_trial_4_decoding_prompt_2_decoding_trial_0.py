# Start the Program

# Receive Input
first_input = input()  # Get the first set of numbers from the user
second_input = input()  # Get the second set of numbers from the user

# Split Input into Individual Numbers
firstSet = first_input.split()  # Break the first set of numbers into a list
secondSet = second_input.split()  # Break the second set of numbers into a list

# Initialize a Difference Counter
differenceCount = 0  # Set a variable called differenceCount to 0

# Compare Corresponding Numbers
for index in range(3):  # For each index from 0 to 2 (inclusive)
    firstNumber = int(firstSet[index])  # Convert the number from firstSet
    secondNumber = int(secondSet[index])  # Convert the number from secondSet
    if firstNumber != secondNumber:  # If numbers are not equal
        differenceCount += 1  # Increment the differenceCount by 1

# Check the Number of Differences
if differenceCount < 3:  # If differenceCount is less than 3
    print("YES")  # Output "YES"
else:  # Otherwise
    print("NO")  # Output "NO"

# End of Program
