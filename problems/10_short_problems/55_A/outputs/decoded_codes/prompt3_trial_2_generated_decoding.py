def find_available_spot():
    # Step 1: Read the input value for 'n'
    n = int(input())
    
    # Step 2: Initialize a list of boolean values
    is_available = [True] * n
    
    # Step 3: Initialize variables for the algorithm
    index = 0
    step = 1

    # Step 4: Start the main loop to iterate up to a defined limit
    while step <= 500000:
        # Step 5: Check if the current index is still available
        if is_available[index]:
            # Mark the current index as unavailable
            is_available[index] = False

        # Step 6: Move to the next step
        step += 1
        
        # Update the index using the modulo operation
        index = (index + step) % n

    # Step 7: Create a list of available spots
    available_spots = [i for i in is_available if i]

    # Step 8: Check if there are any available spots left
    if len(available_spots) == 0:
        # Output result indicating no spots are available
        print('YES')
    else:
        # Output result indicating some spots are available
        print('NO')

# Example of how to call the function
# find_available_spot()
