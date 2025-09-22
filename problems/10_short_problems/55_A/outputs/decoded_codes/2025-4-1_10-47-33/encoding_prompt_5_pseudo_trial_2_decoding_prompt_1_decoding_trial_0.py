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
        booleanList[innerCounter] = False  # Eliminate the element
    outerCounter += 1
    innerCounter = (innerCounter + outerCounter) % n  # Update innerCounter

# Check Remaining Values
remainingTrueValues = [value for value in booleanList if value]

# Determine Result
if len(remainingTrueValues) == 0:
    print('YES')
else:
    print('NO')

# End of the Program
