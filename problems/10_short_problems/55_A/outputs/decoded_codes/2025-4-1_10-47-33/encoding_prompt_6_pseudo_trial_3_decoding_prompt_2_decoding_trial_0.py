# Read an integer input to determine the size of the list
numberOfElements = int(input())

# Initialize a list to track boolean values (True/False) for each position
isActive = [True] * numberOfElements

# Initialize position variables for iterating
index = 0
step = 1

# Loop until the step variable exceeds 500,000
while step <= 500000:
    # Check if the current position in the list is marked as active
    if isActive[index] is True:
        # Mark the current position as inactive
        isActive[index] = False

    # Increment the step variable
    step += 1

    # Update the index based on the step, wrapping around using modulo
    index = (index + step) % numberOfElements

# Filter to create a list of active positions (where value is True)
activePositions = [i for i in isActive if i]

# Check if there are no active positions left
if len(activePositions) == 0:
    print('YES')  # All positions are inactive
else:
    print('NO')   # There are still active (True) positions
