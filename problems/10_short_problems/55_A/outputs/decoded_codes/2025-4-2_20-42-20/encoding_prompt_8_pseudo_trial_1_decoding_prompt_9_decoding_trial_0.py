# Read the size of the list from input
n = int(input())

# Initialize the list with all positions set to True
isActive = [True] * n

# Initialize current position and step count
currentPosition = 0
stepCount = 1

# Loop until stepCount exceeds 500,000
while stepCount <= 500000:
    # Check if the current position is active
    if isActive[currentPosition]:
        # Mark this position as inactive
        isActive[currentPosition] = False
    
    # Increment the step count
    stepCount += 1
    # Update the current position in a wrapping manner
    currentPosition = (currentPosition + stepCount) % n

# Create a list of all positions that are still active
inactivePositions = [index for index, value in enumerate(isActive) if value]

# Output result based on the presence of active positions
if not inactivePositions:
    print("YES")  # All positions got marked inactive
else:
    print("NO")   # At least one position remains active
