# Read Input
n = int(input())

# Initialize List
isActive = [True] * n

# Set Counters
currentPosition = 0
stepCount = 1

# Loop Until Condition Met
while stepCount <= 500000:
    if isActive[currentPosition]:
        isActive[currentPosition] = False  # Mark this position as inactive
    stepCount += 1
    currentPosition = (currentPosition + stepCount) % n  # Wrap around the list

# Check Active Positions
inactivePositions = [i for i in isActive if i]

# Output Result
if not inactivePositions:  # If the list of inactive positions is empty
    print("YES")  # All positions are marked inactive
else:
    print("NO")   # At least one position remains active
