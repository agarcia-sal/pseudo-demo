# Start Program

# Receive Input: 
firstSet = input()            # Read the first set of three numbers
secondSet = input()           # Read the second set of three numbers

# Split Input into Individual Numbers:
firstNumbers = firstSet.split()   # Split firstSet into a list of individual numbers
secondNumbers = secondSet.split()  # Split secondSet into a list of individual numbers

# Initialize Difference Count:
differenceCount = 0                # Set differenceCount to 0

# Compare the Numbers:
for i in range(3):                 # For each position from 0 to 2
    firstNumber = int(firstNumbers[i])      # Convert number at position i in firstNumbers to integer
    secondNumber = int(secondNumbers[i])    # Convert number at position i in secondNumbers to integer
    if firstNumber != secondNumber:          # If firstNumber is not equal to secondNumber
        differenceCount += 1                  # Increment differenceCount by 1

# Evaluate Differences:
if differenceCount < 3:          # If differenceCount is less than 3
    print("YES")                 # Print "YES"
else:                            # Otherwise
    print("NO")                  # Print "NO"

# End Program
