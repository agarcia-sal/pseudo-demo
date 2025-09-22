# Function to determine if all values in the list can be marked as False
def mark_values():
    # Step 2: Get user input for totalCount
    total_count = int(input())
    
    # Step 3: Initialize the list with True values
    is_marked = [True] * total_count
    
    # Step 4: Initialize counters
    current_step = 1
    index = 0
    
    # Step 5: Processing loop
    while current_step <= 500000:
        if is_marked[index]:
            # Mark the current index as processed
            is_marked[index] = False
        
        # Increment current step and update index
        current_step += 1
        index = (index + current_step) % total_count  # Wrap around using modulo
    
    # Step 6: Check remaining True values
    remaining_true = [value for value in is_marked if value]
    
    # Step 7: Determine output
    if len(remaining_true) == 0:
        print("YES")  # All values are marked
    else:
        print("NO")   # Some values remain unmarked

# Step 8: Start the program
mark_values()
