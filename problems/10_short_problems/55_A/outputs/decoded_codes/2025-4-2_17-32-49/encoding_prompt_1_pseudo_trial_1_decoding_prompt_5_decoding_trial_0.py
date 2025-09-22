# Function to check the status of elements after processing
def check_elements_status():
    # Step 1: Read an integer from user input
    n = int(input())

    # Step 2: Initialize a list with 'True' values of size n
    is_not_deleted = [True] * n

    # Step 3: Initialize currentIndex and i
    current_index = 0
    i = 1

    # Step 4: Loop through a specified range
    while i <= 500000:
        # Check if the current index is still marked as 'True'
        if is_not_deleted[current_index]:
            # Mark the element as 'False' (deleted)
            is_not_deleted[current_index] = False
        
        # Increment the loop variable i
        i += 1

        # Update currentIndex, wrap around if needed
        current_index = (current_index + i) % n

    # Step 5: Check for remaining 'True' values
    remaining_true = [value for value in is_not_deleted if value]

    # Step 6: Determine output based on remaining values
    if len(remaining_true) == 0:
        print('YES')
    else:
        print('NO')

# Call the function to execute it
check_elements_status()
