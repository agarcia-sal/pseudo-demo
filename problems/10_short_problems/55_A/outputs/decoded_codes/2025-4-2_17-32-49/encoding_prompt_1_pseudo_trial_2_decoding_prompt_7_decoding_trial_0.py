# Step 1: Read an integer value n from user input
n = int(input())

# Step 2: Initialization
# Create a list isPresent of size n, initialized with True
isPresent = [True] * n
# Initialize index and step
index = 0
step = 1

# Step 3: Processing Loop
# Repeat the following steps while step is less than or equal to 500,000
while step <= 500000:
    # If the current position is available
    if isPresent[index]:
        # Mark this position as not available
        isPresent[index] = False
    
    # Increment the step
    step += 1
    # Update index to the next position, wrapping around using modulo
    index = (index + step) % n

# Step 4: Checking Results
# Create a new list of available positions
availablePositions = [i for i in isPresent if i]

# If there are no available positions
if len(availablePositions) == 0:
    print("YES")  # All positions have been marked as not available
else:
    print("NO")   # There are still available positions
