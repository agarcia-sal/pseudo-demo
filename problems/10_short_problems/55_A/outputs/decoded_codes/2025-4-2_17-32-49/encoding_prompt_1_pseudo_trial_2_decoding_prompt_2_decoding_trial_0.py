# Input
n = int(input())

# Initialization
isPresent = [True] * n  # Create a list of size n initialized with True
index = 0
step = 1

# Processing Loop
while step <= 500000:
    if isPresent[index]:  # Check if the current position is available
        isPresent[index] = False  # Mark this position as not available
    
    step += 1  # Increment step
    index = (index + step) % n  # Update index for the next position

# Checking Results
availablePositions = [pos for pos in isPresent if pos]  # Extract available positions
if len(availablePositions) == 0:
    print("YES")  # All positions are marked as not available
else:
    print("NO")  # There are still available positions
