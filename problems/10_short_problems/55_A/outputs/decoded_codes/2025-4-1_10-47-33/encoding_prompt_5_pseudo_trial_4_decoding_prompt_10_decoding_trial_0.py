def main():
    # Step 1: Get user input for the number of slots
    number_of_slots = int(input())

    # Step 2: Initialize a list to keep track of available slots
    is_available = [True] * number_of_slots  # True indicates the slot is available

    # Step 3: Initialize counters for processing
    step_increment = 1  # Determines the next slot to mark as not available
    current_index = 0  # Tracks the current position in the list

    # Step 4: Begin the process of marking slots
    while step_increment <= 500000:
        # Check if the current slot is still available
        if is_available[current_index]:
            # Mark the current slot as not available
            is_available[current_index] = False
        
        # Move to the next step
        step_increment += 1
        current_index = (current_index + step_increment) % number_of_slots

    # Step 5: Check for remaining available slots
    remaining_available_slots = [slot for slot in is_available if slot]

    # Step 6: Determine the output based on available slots
    if len(remaining_available_slots) == 0:
        print("YES")  # No slots are available
    else:
        print("NO")  # There are still available slots

# Call the main function to execute the program
if __name__ == "__main__":
    main()
