# Step 1: Read an integer value n from user input
n = int(input())

# Step 2: Initialize a list isPresent of size n, filled with True
is_present = [True] * n

# Step 2: Initialize index and step variables
index = 0
step = 1

# Step 3: Processing Loop
while step <= 500000:
    if is_present[index]:  # Check if the current position is available
        is_present[index] = False  # Mark the position as not available

    step += 1  # Increment step
    index = (index + step) % n  # Calculate the next index in a circular manner

# Step 4: Check results
available_positions = [pos for pos in is_present if pos]  # Collect all available positions
if len(available_positions) == 0:
    print("YES")  # All positions are marked as not available
else:
    print("NO")  # There are still available positions
