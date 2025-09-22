# Step 1: Initialize the Program
n = int(input())

# Step 2: Create a boolean list
isActive = [True] * n

# Step 3: Set initial positions
index = 0  # Current position in the list
step = 1   # Steps to move after each iteration

# Step 4: Iterate through steps
while step <= 500000:
    if isActive[index]:  # Check if the current position is active
        isActive[index] = False  # Deactivate the current position
    step += 1  # Increment step
    index = (index + step) % n  # Update index with wrap-around

# Step 5: Check remaining active positions
activePositions = [active for active in isActive if active]

# Step 6: Determine the output
if len(activePositions) == 0:
    print("YES")  # All positions have been deactivated
else:
    print("NO")   # There are still active positions
