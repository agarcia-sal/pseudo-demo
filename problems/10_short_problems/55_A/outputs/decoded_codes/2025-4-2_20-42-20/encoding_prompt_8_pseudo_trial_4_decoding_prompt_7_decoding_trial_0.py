# Step 1: Get input
n = int(input())  # Read a number n from the user representing the size of the list

# Step 2: Initialize a boolean list
positions = [True] * n  # Create a list of size n with all elements set to True

# Step 3: Index variables
currentIndex = 0  # Set variable currentIndex to 0
step = 1  # Set variable step to 1

# Step 4: Loop through positions
while step <= 500000:
    # Check if the current position in positions is True
    if positions[currentIndex]:
        positions[currentIndex] = False  # Mark the position as False

    # Increment step and update currentIndex
    step += 1  # Increase step by 1
    currentIndex = (currentIndex + step) % n  # Update currentIndex with wrap around

# Step 5: Check for unmarked positions
unmarkedPositions = [pos for pos in positions if pos]  # Create a list of all True positions

# Step 6: Output the result
if len(unmarkedPositions) == 0:  # Check if there are no unmarked positions
    print('YES')  # If all positions are marked
else:
    print('NO')  # If there are still unmarked positions
