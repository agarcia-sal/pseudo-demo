def main():
    # Step 2: Get user input
    total_count = int(input())
    
    # Step 3: Initialize the list
    is_marked = [True] * total_count
    
    # Step 4: Set counters
    current_step = 1
    index = 0
    
    # Step 5: Processing loop
    while current_step <= 500000:
        if is_marked[index]:
            # Mark this position as processed
            is_marked[index] = False
        
        # Increment current step and update index
        current_step += 1
        index = (index + current_step) % total_count
    
    # Step 6: Check results
    remaining_true = [x for x in is_marked if x]

    # Step 7: Determine output
    if len(remaining_true) == 0:
        print("YES")  # All positions marked
    else:
        print("NO")   # Some positions remain unmarked

# Step 8: End the program
if __name__ == "__main__":
    main()
