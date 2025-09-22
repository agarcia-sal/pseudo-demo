# Step 1: Read Input
n = int(input())

# Step 2: Initialize List
isActive = [True] * n  # Create a list of size n filled with True

# Step 3: Set Counters
currentPosition = 0
stepCount = 1

# Step 4: Loop Until Condition Met
while stepCount <= 500000:
    if isActive[currentPosition]:  # If the current position is active
        isActive[currentPosition] = False  # Mark it as inactive
    stepCount += 1  # Increment the step count
    currentPosition = (currentPosition + stepCount) % n  # Update position with wrap-around

# Step 5: Check Active Positions
inactivePositions = [i for i in isActive if i]  # Collect all positions that are still True

# Step 6: Output Result
if not inactivePositions:  # If the inactivePositions list is empty
    print("YES")  # All positions are inactive
else:
    print("NO")  # At least one position remains active
