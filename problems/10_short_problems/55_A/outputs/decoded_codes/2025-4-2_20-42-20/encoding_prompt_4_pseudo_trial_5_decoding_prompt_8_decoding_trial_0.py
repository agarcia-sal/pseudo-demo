# INPUT: An integer n from user
n = int(input())

# Initialize a list of boolean values to True for the range 0 to n
isActive = [True] * n

# Initialize indices
j = 0  # Current index
i = 1  # Step increment

# Loop until i exceeds 500,000
while i <= 500000:
    # If the current position is active
    if isActive[j]:
        # Deactivate current position
        isActive[j] = False
    
    # Increment step by 1
    i += 1
    
    # Update index j in circular manner
    j = (j + i) % n

# Create a list of active positions
activePositions = [index for index, value in enumerate(isActive) if value]

# Check if there are any active positions
if len(activePositions) == 0:
    # If no active positions remain
    print('YES')
else:
    # If there are still active positions
    print('NO')
