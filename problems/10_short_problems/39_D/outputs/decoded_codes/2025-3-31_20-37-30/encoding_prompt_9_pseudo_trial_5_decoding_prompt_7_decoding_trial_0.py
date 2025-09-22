# Start the program

# Step 2: Receive Input
firstSet = input()  # Read the first set of numbers from the user
secondSet = input()  # Read the second set of numbers from the user

# Step 3: Process Input
firstNumbers = firstSet.split()  # Split firstSet into a list called firstNumbers
secondNumbers = secondSet.split()  # Split secondSet into a list called secondNumbers

# Step 4: Initialize Differences Counter
differenceCount = 0  # Set differenceCount to 0 to track differences

# Step 5: Compare Numbers
for index in range(3):  # Loop through indices 0 to 2
    firstNumber = int(firstNumbers[index])  # Convert firstNumber from firstNumbers to int
    secondNumber = int(secondNumbers[index])  # Convert secondNumber from secondNumbers to int
    if firstNumber != secondNumber:  # Check if the numbers are different
        differenceCount += 1  # Increase differenceCount by 1 if they differ

# Step 6: Determine Output
if differenceCount < 3:  # Check if differences are less than 3
    print("YES")  # Print "YES" if true
else:
    print("NO")  # Print "NO" if false

# End the program
