def main():
    # Step 2: Input an integer value 'n'
    n = int(input())
    
    # Step 3: Initialize a list 'isActive' with True values
    is_active = [True] * n
    
    # Step 4: Set initial variables
    next_index = 0
    current_step = 1
    
    # Step 5: Loop until 'currentStep' exceeds 500,000
    while current_step <= 500000:
        if is_active[next_index]:  # Check if the current index is active
            is_active[next_index] = False  # Mark as inactive
        
        # Increment current step
        current_step += 1
        
        # Update nextIndex and wrap around using modulo
        next_index = (next_index + current_step) % n
    
    # Step 6: Filter active elements
    active_elements = [index for index in range(n) if is_active[index]]
    
    # Step 7: Output the result
    if len(active_elements) == 0:
        print("YES")  # If no active elements are left
    else:
        print("NO")   # Active elements remain

# Step 1: Start the program
if __name__ == "__main__":
    main()
