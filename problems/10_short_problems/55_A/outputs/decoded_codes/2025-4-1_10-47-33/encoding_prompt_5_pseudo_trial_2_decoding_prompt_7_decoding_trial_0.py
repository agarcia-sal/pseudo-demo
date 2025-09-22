# Start of the Program
# Get the size of the list from user input
n = int(input())

# Initialize a list with n elements, all set to True (not eliminated)
booleanList = [True] * n

# Set up counters
outerCounter = 1  # starts at 1
innerCounter = 0  # starts at 0

# Elimination loop
while outerCounter <= 500000:
    # Check if the current index in booleanList is True
    if booleanList[innerCounter]:
        # Eliminate the current element
        booleanList[innerCounter] = False
    
    # Increase outerCounter for the next iteration
    outerCounter += 1
    
    # Update innerCounter: wrap around with modulus to keep it within bounds of booleanList
    innerCounter = (innerCounter + outerCounter) % n

# Check remaining True values
remainingTrueValues = [value for value in booleanList if value]

# Determine result
if len(remainingTrueValues) == 0:
    print('YES')  # All values have been eliminated
else:
    print('NO')   # Some values are still True

# End of the Program
