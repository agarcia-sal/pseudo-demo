# Initialize the Program
n = int(input())

# Create a boolean list
isActive = [True] * n

# Set initial positions
index = 0
step = 1

# Iterate through steps
while step <= 500000:
    if isActive[index]:  # Check if the current position is True
        isActive[index] = False  # Deactivate the position
    step += 1
    index = (index + step) % n  # Update the index, wrapping around using modulo

# Check remaining active positions
activePositions = [pos for pos in isActive if pos]

# Determine the output
if len(activePositions) == 0:  # No True values are left
    print("YES")
else:
    print("NO")
