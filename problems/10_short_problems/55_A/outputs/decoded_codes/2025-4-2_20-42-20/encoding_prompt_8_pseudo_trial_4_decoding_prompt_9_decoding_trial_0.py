# Get input from the user
n = int(input())  # Read a number representing the size of the list

# Initialize a boolean list
positions = [True] * n  # Create a list of size n with all positions initially set to True

# Index variables
currentIndex = 0  # This will track the current position being processed
step = 1  # This determines how far to move in the list during each iteration

# Loop through positions with the maximum step limit
while step <= 500000:
    # Check if the current position is still marked as True
    if positions[currentIndex]:
        positions[currentIndex] = False  # Set it to False, indicating it has been marked
    
    # Increment the step to change the movement for the next iteration
    step += 1
    # Update the currentIndex using modulo to wrap around the list
    currentIndex = (currentIndex + step) % n

# Create a list of unmarked positions (still True)
unmarkedPositions = [pos for pos in positions if pos]

# Check if all positions have been marked
if len(unmarkedPositions) == 0:
    print('YES')  # All positions are marked
else:
    print('NO')  # There are unmarked positions
