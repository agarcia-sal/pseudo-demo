# Step 1: Get user input for the number of slots
number_of_slots = int(input())

# Step 2: Initialize a list to keep track of available slots
is_available = [True] * number_of_slots  # Create a list filled with True

# Step 3: Initialize counters for processing
step_increment = 1  # This will be used to determine the next slot to mark as not available
current_index = 0   # This will track the current position in the list

# Step 4: Begin the process of marking slots
while step_increment <= 500000:  # Continue until step_increment exceeds 500000
    # Check if the current slot is still available
    if is_available[current_index]:  # if is_available[current_index] is True
        is_available[current_index] = False  # Mark the current slot as not available

    # Move to the next step
    step_increment += 1  # Increment step_increment by 1
    current_index = (current_index + step_increment) % number_of_slots  # Update current_index

# Step 5: Check for remaining available slots
remaining_available_slots = [slot for slot in is_available if slot]  # Create a list of True values

# Step 6: Determine the output based on available slots
if len(remaining_available_slots) == 0:  # If no available slots are left
    print("YES")  # Output "YES" if no slots are available
else:
    print("NO")  # Output "NO" if there are still available slots
