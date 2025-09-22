# Step 1: Read Input
n = int(input())

# Step 2: Initialize List
marked = [True] * n  # Create a list with n elements set to True

# Step 3: Initialize Counters
current_index = 0  # This will represent the position currently being processed
step_size = 1      # This will be the increment for marking

# Step 4: Iterative Marking
while step_size <= 500000:
    if marked[current_index]:  # If the current position is marked True
        marked[current_index] = False  # Mark it as False
    step_size += 1  # Increment the step size
    current_index = (current_index + step_size) % n  # Calculate the next position

# Step 5: Check Marks
remaining_true = [mark for mark in marked if mark]  # Create a list of remaining True elements

# Step 6: Output Result
if len(remaining_true) == 0:  # If all were marked
    print("YES")
else:
    print("NO")
