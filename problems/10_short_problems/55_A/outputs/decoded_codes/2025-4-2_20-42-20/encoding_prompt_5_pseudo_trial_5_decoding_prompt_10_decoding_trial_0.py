def main():
    # Step 1: Get Number of Elements
    n = int(input())
    
    # Step 2: Initialize List
    is_active = [True] * n  # Create a list with n elements, all set to True
    
    # Step 3: Set Initial Indices
    current_index = 0
    step = 1
    
    # Step 4: Process the List
    while step <= 500000:
        if is_active[current_index]:  # Check if the current element is active
            is_active[current_index] = False  # Mark this element as inactive

        step += 1  # Increment the step for the next iteration
        current_index = (current_index + step) % n  # Update the current index cyclically

    # Step 5: Check Remaining Active Elements
    remaining_active = [active for active in is_active if active]
    
    # Step 6: Output Result
    if len(remaining_active) == 0:  # If no active elements left
        print("YES")
    else:
        print("NO")

# This code will be executed when the script is run directly
if __name__ == "__main__":
    main()
