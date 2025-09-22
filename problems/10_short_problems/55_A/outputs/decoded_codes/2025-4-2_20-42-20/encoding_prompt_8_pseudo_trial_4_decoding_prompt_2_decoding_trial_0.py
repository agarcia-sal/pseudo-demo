# Step 1: Get input
n = int(input())  # Read a number n from the user

# Step 2: Initialize a boolean list
positions = [True] * n  # Create a list of size n with all values set to True

# Step 3: Index variables
currentIndex = 0  # Variable to track the current position being processed
step = 1          # Variable to determine how far to move in the list during each iteration

# Step 4: Loop through positions
while step <= 500000:
    if positions[currentIndex]:  # Check if the current position is True
        positions[currentIndex] = False  # Mark the position as False

    step += 1  # Increment step by 1
    currentIndex = (currentIndex + step) % n  # Update currentIndex using modulo n

# Step 5: Check for unmarked positions
unmarkedPositions = [p for p in positions if p]  # Create a list of all True positions

# Step 6: Output the result
if len(unmarkedPositions) == 0:  # If all positions have been marked
    print('YES')
else:
    print('NO')
