def main():
    # Step 1: Read the number of elements
    number_of_elements = int(input())
    
    # Step 2: Initialize the list with True values
    is_active = [True] * number_of_elements
    
    # Initialize variables
    index = 0
    step = 1

    # Step 4: Process until step exceeds 500000
    while step <= 500000:
        if is_active[index]:  # Step 4a
            is_active[index] = False  # Step 4ai: Marking index as inactive
        step += 1  # Step 4b: Increment step
        index = (index + step) % number_of_elements  # Step 4c: Calculate new index

    # Step 5: Collect all active elements
    active_elements = [active for active in is_active if active]

    # Step 6: Determine if there are any active elements left
    if len(active_elements) == 0:  # Step 6a
        print('YES')  # No active elements remaining
    else:  # Step 6b
        print('NO')  # There are active elements remaining

# Entry point for the script
if __name__ == "__main__":
    main()
