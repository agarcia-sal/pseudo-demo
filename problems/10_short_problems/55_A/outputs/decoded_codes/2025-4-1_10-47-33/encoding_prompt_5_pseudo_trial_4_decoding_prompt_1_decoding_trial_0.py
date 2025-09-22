# Step 1: Get user input for the number of slots
NUMBER_OF_SLOTS = int(input())

# Step 2: Initialize a list to keep track of available slots
IS_AVAILABLE = [True] * NUMBER_OF_SLOTS

# Step 3: Initialize counters for processing
step_increment = 1  # This will be used to determine the next slot to mark as not available
current_index = 0   # This will track the current position in the list

# Step 4: Begin the process of marking slots
while step_increment <= 500000:
    # Check if the current slot is still available
    if IS_AVAILABLE[current_index] is True:
        # Mark the current slot as not available
        IS_AVAILABLE[current_index] = False

    # Move to the next step
    step_increment += 1
    current_index = (current_index + step_increment) % NUMBER_OF_SLOTS

# Step 5: Check for remaining available slots
remaining_available_slots = [slot for slot in IS_AVAILABLE if slot is True]

# Step 6: Determine the output based on available slots
if len(remaining_available_slots) == 0:
    print("YES")  # No slots are available
else:
    print("NO")   # There are still available slots
