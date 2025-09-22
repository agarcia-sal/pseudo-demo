# BEGIN

# Read an integer input which defines the size of an array
arraySize = int(input())

# Initialize a list of boolean values, indicating active status
booleanList = [True] * arraySize

# Initialize counters
indexCounter = 0
stepIncrement = 1

# Loop until stepIncrement exceeds 500000
while stepIncrement <= 500000:
    
    # If the current position in the boolean list is True
    if booleanList[indexCounter] is True:
        
        # Mark this position as False, indicating it's been processed
        booleanList[indexCounter] = False

    # Increment stepIncrement after processing
    stepIncrement += 1
    
    # Update the indexCounter using modulo to stay within bounds of boolean list length
    indexCounter = (indexCounter + stepIncrement) % arraySize

# Create a new list containing only True values remaining in the boolean list
activeItems = [value for value in booleanList if value]

# Check if there are no True values remaining
if len(activeItems) == 0:
    print("YES")
else:
    print("NO")

# END
