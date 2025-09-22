def check_all_numbers_removed(n):
    # Initialize a list to track removed numbers, all set to True initially
    is_removed = [True] * n
    current_index = 0
    current_step = 1

    # Loop until the current step exceeds 500,000
    while current_step <= 500000:
        # Mark the current index as removed (set to False)
        if is_removed[current_index]:
            is_removed[current_index] = False
            
        # Move to the next step
        current_step += 1
        current_index = (current_index + current_step) % n
    
    # Check for any remaining numbers that are not removed
    remaining = [value for value in is_removed if value]

    # Print 'YES' if no numbers are remaining, otherwise print 'NO'
    if not remaining:
        print('YES')
    else:
        print('NO')

# Test cases to validate the function
if __name__ == "__main__":
    # Example test case
    n = int(input())
    check_all_numbers_removed(n)

    # Additional tests can be added as needed
