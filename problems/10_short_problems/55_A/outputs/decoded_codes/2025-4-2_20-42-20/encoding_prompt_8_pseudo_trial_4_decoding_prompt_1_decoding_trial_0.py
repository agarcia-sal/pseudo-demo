# Step 1: Get input
n = int(input())  # Read a number n from the user for the size of the list

# Step 2: Initialize a boolean list
positions = [True] * n  # Create a list of size n with all True values

# Step 3: Index variables
currentIndex = 0  # Tracking the current position
step = 1  # The step size for movements

# Step 4: Loop through positions
while step <= 500000:
    if positions[currentIndex]:  # Check if the current position is True
        positions[currentIndex] = False  # Mark the position as False
    
    step += 1  # Increment the step
    currentIndex = (currentIndex + step) % n  # Update the current index

# Step 5: Check for unmarked positions
unmarkedPositions = [pos for pos in positions if pos]  # Collect all True positions

# Step 6: Output the result
if len(unmarkedPositions) == 0:  # If all positions are marked
    print('YES')
else:
    print('NO')
