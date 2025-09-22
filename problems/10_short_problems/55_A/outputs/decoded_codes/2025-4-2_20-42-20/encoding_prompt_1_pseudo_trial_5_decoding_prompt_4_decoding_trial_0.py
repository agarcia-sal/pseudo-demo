def main():
    # Step 2: Input the integer number n from user
    n = int(input())
    
    # Step 3: Initialize the status list with n elements set to True
    status = [True] * n
    
    # Step 4: Set initial counter and index
    current_step = 1
    index = 0
    
    # Step 5: Loop until current_step exceeds 500000
    while current_step <= 500000:
        # Step 5.1: Check status at the current index
        if status[index]:
            status[index] = False  # Mark this index as False (not active)
        
        # Step 5.2: Increment the step
        current_step += 1
        
        # Step 5.3: Update index using modulus
        index = (index + current_step) % n
    
    # Step 6: Filter active status (elements still True)
    active_elements = [s for s in status if s]
    
    # Step 7: Check the result and print accordingly
    if len(active_elements) == 0:
        print("YES")  # All elements are inactive
    else:
        print("NO")   # There are some active elements

# Call the main function to execute
main()
