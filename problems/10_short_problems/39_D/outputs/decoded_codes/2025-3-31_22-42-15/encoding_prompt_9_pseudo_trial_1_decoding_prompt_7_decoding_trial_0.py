# Start Program

# Step 2: Receive Input
# Read the first set of three numbers from the user and store it in a variable named firstSet
firstSet = input()
# Read the second set of three numbers from the user and store it in a variable named secondSet
secondSet = input()

# Step 3: Split Input into Individual Numbers
# Split firstSet into a list of individual numbers called firstNumbers
firstNumbers = firstSet.split()
# Split secondSet into a list of individual numbers called secondNumbers
secondNumbers = secondSet.split()

# Step 4: Initialize Difference Count
# Set a variable named differenceCount to 0
differenceCount = 0

# Step 5: Compare the Numbers
# For each position from 0 to 2 (representing the three numbers)
for i in range(3):
    # Convert the number at that position in firstNumbers to an integer
    firstNumber = int(firstNumbers[i])
    # Convert the number at that position in secondNumbers to an integer
    secondNumber = int(secondNumbers[i])
    
    # If firstNumber is not equal to secondNumber
    if firstNumber != secondNumber:
        # Increment differenceCount by 1
        differenceCount += 1

# Step 6: Evaluate Differences
# If differenceCount is less than 3
if differenceCount < 3:
    # Print "YES"
    print("YES")
else:
    # Otherwise, print "NO"
    print("NO")

# End Program
