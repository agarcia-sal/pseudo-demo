# Step 1: Read Input
n = int(input())  # Get the size of the list

# Step 2: Initialize List
isActive = [True] * n  # Create a list of size n filled with True

# Step 3: Set Counters
currentPosition = 0  # Start at the first position
stepCount = 1  # Step size begins at 1

# Step 4: Loop Until Condition Met
while stepCount <= 500000:  # Maximum of 500,000 steps
    if isActive[currentPosition]:  # Check if the current position is active
        isActive[currentPosition] = False  # Mark this position as inactive
    
    stepCount += 1  # Increment the step size
    currentPosition = (currentPosition + stepCount) % n  # Update position, wrapping around using modulo

# Step 5: Check Active Positions
inactivePositions = [pos for pos in isActive if pos]  # Gather all positions that are still active (True)

# Step 6: Output Result
if not inactivePositions:  # If there are no active positions
    print("YES")  # All positions marked inactive
else:
    print("NO")  # At least one position remains active
