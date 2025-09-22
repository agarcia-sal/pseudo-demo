# Step 1: Input
n = int(input())

# Step 2: Initialization
isPresent = [True] * n  # Create a list of size n initialized with True
index = 0
step = 1

# Step 3: Processing Loop
while step <= 500000:
    if isPresent[index]:  # Check if the position is available
        isPresent[index] = False  # Mark position as not available
    
    step += 1  # Increment step
    index = (index + step) % n  # Update index with wrapping

# Step 4: Checking Results
availablePositions = [pos for pos in isPresent if pos]  # Create list of available positions

if len(availablePositions) == 0:
    print("YES")  # All positions are not available
else:
    print("NO")   # There are still available positions
