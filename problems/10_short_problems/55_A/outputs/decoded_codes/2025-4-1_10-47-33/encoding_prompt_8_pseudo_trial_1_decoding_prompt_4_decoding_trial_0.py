def main():
    # Step 2: Get Input
    n = int(input())

    # Step 3: Initialize List
    is_marked = [True] * n  # Start with all items unmarked (True)

    # Step 4: Initialize Counters
    current_index = 0
    increment = 1

    # Step 5: Marking Process
    while increment <= 500000:
        # If the current item is still marked as True
        if is_marked[current_index]:
            # Mark this item as processed
            is_marked[current_index] = False
        
        # Increment the step size for the next marking operation
        increment += 1
        
        # Update current_index with wrapping
        current_index = (current_index + increment) % n
    
    # Step 6: Check for Unmarked Items
    unmarked_items = [item for item in is_marked if item]  # Collect all unmarked items

    # Step 7: Output Result
    if len(unmarked_items) == 0:
        print('YES')  # All items are marked
    else:
        print('NO')   # There are unmarked items

# Step 1: Start Program
if __name__ == "__main__":
    main()
