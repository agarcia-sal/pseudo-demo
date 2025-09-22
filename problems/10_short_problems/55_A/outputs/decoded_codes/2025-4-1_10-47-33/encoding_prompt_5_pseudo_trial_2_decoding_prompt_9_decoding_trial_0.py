# Start of the Program
n = int(input())  # Get the size of the list from user input

# Initialize a List
booleanList = [True] * n  # Create a list with n elements all set to True

# Set Up Counters
outerCounter = 1
innerCounter = 0

# Elimination Loop
while outerCounter <= 500000:
    if booleanList[innerCounter]:  # Check if the current element is True
        booleanList[innerCounter] = False  # Eliminate it by setting it to False
    
    outerCounter += 1  # Increase the outer counter
    
    # Update the inner counter cyclically
    innerCounter = (innerCounter + outerCounter) % n

# Check Remaining Values
remainingTrueValues = [val for val in booleanList if val]  # List of remaining True values

# Determine Result
if len(remainingTrueValues) == 0:  # If there are no True values left
    print('YES')  # Output YES indicating all values have been eliminated
else:
    print('NO')  # Output NO indicating some values are still True
