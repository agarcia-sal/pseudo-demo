# Start the program

# Receive Input
firstSet = input()  # Read the first set of numbers
secondSet = input()  # Read the second set of numbers

# Process Input
firstNumbers = firstSet.split()  # Split the first set into a list of numbers
secondNumbers = secondSet.split()  # Split the second set into a list of numbers

# Initialize Differences Counter
differenceCount = 0  # Counter for differences

# Compare Numbers
for index in range(3):  # Loop through indices 0 to 2
    firstNumber = int(firstNumbers[index])  # Convert the first number to integer
    secondNumber = int(secondNumbers[index])  # Convert the second number to integer
    
    if firstNumber != secondNumber:  # Check if they differ
        differenceCount += 1  # Increase the counter if they differ

# Determine Output
if differenceCount < 3:  # If differences are fewer than 3
    print("YES")  # Output "YES"
else:
    print("NO")  # Output "NO"

# End the program
