# Read an integer input representing the size of the list
n = int(input())

# Create a boolean list initialized to True with size n
is_active = [True] * n

# Initialize index variables for operation
current_index = 0
step = 1

# Loop until step exceeds 500,000
while step <= 500000:
    # If the current position in the list is marked True
    if is_active[current_index]:
        # Mark the current position as False
        is_active[current_index] = False

    # Increment step counter
    step += 1
    
    # Update currentIndex using modulo operation for wrapping
    current_index = (current_index + step) % n

# Filter the list to find all active positions (True values)
active_positions = [i for i in is_active if i]

# Check if there are no active positions remaining
if len(active_positions) == 0:
    print('YES')  # No active positions remain
else:
    print('NO')   # There are active positions remaining
