# Initialize the Program
n = int(input())  # Read an integer value n from user input

# Create a boolean list
is_active = [True] * n  # List named is_active with n elements initialized to True

# Set initial positions
index = 0  # Variable to track the current position in the list
step = 1   # Variable to determine how many steps to move after each iteration

# Iterate through steps
while step <= 500000:
    if is_active[index]:  # Check if the current position is True
        is_active[index] = False  # Set that position to False
    step += 1  # Increment step by 1
    index = (index + step) % n  # Update index and wrap around if it exceeds n

# Check remaining active positions
active_positions = [pos for pos in is_active if pos]  # List of still active (True) positions

# Determine the output
if len(active_positions) == 0:  # If no True values are left
    print("YES")  # Print "YES" indicating all positions are deactivated
else:
    print("NO")  # Print "NO" indicating some positions are still active
