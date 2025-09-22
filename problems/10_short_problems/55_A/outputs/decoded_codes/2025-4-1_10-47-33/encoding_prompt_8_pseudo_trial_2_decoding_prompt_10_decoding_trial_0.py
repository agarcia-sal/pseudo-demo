def main():
    # Step 1: Get Input
    n = int(input())
    
    # Step 2: Initialize List of booleans
    is_active = [True] * n
    
    # Step 3: Initialize Counters
    current_index = 0
    step_number = 1
    
    # Step 4: Iterate to Modify List
    while step_number <= 500000:
        if is_active[current_index]:
            is_active[current_index] = False  # Mark the current index as inactive
        
        step_number += 1
        current_index = (current_index + step_number) % n  # Update index, wrapping around using modulo
    
    # Step 5: Check Remaining Active Elements
    remaining_active = [status for status in is_active if status]
    
    # Step 6: Determine Output
    if len(remaining_active) == 0:
        print("YES")  # All elements have been changed to False
    else:
        print("NO")   # At least one element remains True

if __name__ == "__main__":
    main()
