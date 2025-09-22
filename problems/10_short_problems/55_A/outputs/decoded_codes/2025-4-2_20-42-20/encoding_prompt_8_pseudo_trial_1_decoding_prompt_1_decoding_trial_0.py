# Read Input
n = int(input())

# Initialize List
isActive = [True] * n  # List of size n filled with True

# Set Counters
currentPosition = 0  # Current position in the list
stepCount = 1        # Step size for iteration

# Loop Until Condition Met
while stepCount <= 500000:
    if isActive[currentPosition]:  # Check if current position is active
        isActive[currentPosition] = False  # Mark position as inactive
    stepCount += 1  # Increment step count
    currentPosition = (currentPosition + stepCount) % n  # Update position with wrap-around

# Check Active Positions
inactivePositions = [i for i in isActive if i]  # List of positions that are still True

# Output Result
if not inactivePositions:  # If no positions remain active
    print("YES")  # All positions marked inactive
else:
    print("NO")  # At least one position remains active
