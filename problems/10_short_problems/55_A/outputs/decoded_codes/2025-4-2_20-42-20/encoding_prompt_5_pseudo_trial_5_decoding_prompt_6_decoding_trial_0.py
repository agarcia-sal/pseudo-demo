# Step 1: Get Number of Elements
n = int(input())  # Read an integer value representing the number of elements

# Step 2: Initialize List
is_active = [True] * n  # Create a list with n True elements

# Step 3: Set Initial Indices
current_index = 0  # Starting index pointing to the first element
step = 1  # Step variable starting at 1

# Step 4: Process the List
while step <= 500000:  # Repeat until step exceeds 500,000
    if is_active[current_index]:  # Check if the current element is True
        is_active[current_index] = False  # Mark it as False
    current_index = (current_index + step) % n  # Update current index with wrapping
    step += 1  # Increment the step for the next iteration

# Step 5: Check Remaining Active Elements
remaining_active = [active for active in is_active if active]  # Filter list for True values

# Step 6: Output Result
if len(remaining_active) == 0:  # Check if there are no active elements left
    print("YES")  # Print YES if no active elements
else:
    print("NO")  # Print NO if there are still active elements
