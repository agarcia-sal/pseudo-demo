# Step 1: Accept an integer input which defines the size of the boolean list
n = int(input())

# Step 2: Initialize a boolean list with 'True' values to represent the flags
is_active = [True] * n

# Step 3: Initialize variables for tracking current index and iteration count
current_index = 0
iteration_count = 1

# Step 4: Perform a loop to process flags based on the specified conditions
while iteration_count <= 500000:
    # Step 4.1: Check if the flag at the current index is active
    if is_active[current_index]:
        # Step 4.2: Deactivate the current flag
        is_active[current_index] = False

    # Step 4.3: Move to the next index based on the current iteration count
    iteration_count += 1
    current_index = (current_index + iteration_count) % n

# Step 5: Create a new list of active flags
active_flags = [flag for flag in is_active if flag]

# Step 6: Check if there are any active flags left
if len(active_flags) == 0:
    # If no flags are active, print "YES"
    print("YES")
else:
    # If there are still active flags, print "NO"
    print("NO")
