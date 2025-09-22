# Start of the Program
n = int(input())

# Initialize a List
booleanList = [True] * n

# Set Up Counters
outerCounter = 1
innerCounter = 0

# Elimination Loop
while outerCounter <= 500000:
    if booleanList[innerCounter]:
        booleanList[innerCounter] = False  # Eliminate the current element

    outerCounter += 1
    innerCounter = (innerCounter + outerCounter) % n  # Update the inner counter

# Check Remaining Values
remainingTrueValues = [value for value in booleanList if value]

# Determine Result
if len(remainingTrueValues) == 0:
    print('YES')  # All values have been eliminated
else:
    print('NO')  # Some values are still True

# End of the Program
