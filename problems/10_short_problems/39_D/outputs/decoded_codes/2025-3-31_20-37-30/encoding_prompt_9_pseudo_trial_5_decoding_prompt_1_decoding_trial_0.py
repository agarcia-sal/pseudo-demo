# 1. Start the program.

# 2. Receive Input:
firstSet = input()  # Read the first set of numbers
secondSet = input()  # Read the second set of numbers

# 3. Process Input:
firstNumbers = firstSet.split()  # Split firstSet into a list of individual numbers
secondNumbers = secondSet.split()  # Split secondSet into a list of individual numbers

# 4. Initialize Differences Counter:
differenceCount = 0  # Set the difference count to 0

# 5. Compare Numbers:
for index in range(3):  # Loop through indices 0 to 2
    firstNumber = int(firstNumbers[index])  # Convert number at current index from firstNumbers to integer
    secondNumber = int(secondNumbers[index])  # Convert number at current index from secondNumbers to integer
    if firstNumber != secondNumber:  # Check if numbers are different
        differenceCount += 1  # Increase the difference count by 1

# 6. Determine Output:
if differenceCount < 3:  # Check if difference count is less than 3
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"

# 7. End the program.
