def mark_elements():
    # Step 2: Receive Input
    n = int(input())  # Read the size of the list

    # Step 3: Initialize Boolean List
    boolean_list = [True] * n  # All positions initially unmarked (True)

    # Step 4: Set Up Iteration Variables
    current_index = 0  # Track the current position in boolean_list
    step = 1  # Starting step value

    # Step 5: Mark Elements Process
    while step <= 500000:
        # Step 5.1: Check Current Position
        if boolean_list[current_index]:
            # Mark the current position as False (indicating it is now marked)
            boolean_list[current_index] = False

        # Step 5.2: Increment Step Value
        step += 1

        # Step 5.3: Calculate Next Position
        current_index = (current_index + step) % n  # Wraps around if exceeds length

    # Step 6: Extract Remaining Unmarked Elements
    remaining_true = [value for value in boolean_list if value]

    # Step 7: Check Results
    if len(remaining_true) == 0:
        print("YES")  # All positions were marked
    else:
        print("NO")   # There are unmarked positions

# Call the function to execute
mark_elements()
