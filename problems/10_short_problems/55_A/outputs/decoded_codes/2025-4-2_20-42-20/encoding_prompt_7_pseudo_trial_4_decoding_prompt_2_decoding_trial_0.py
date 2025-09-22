def check_consecutive_numbers(n):
    # Initialize an array 'is_true' of size n with all values set to True
    is_true = [True] * n
    j = 0  # Initialize index 'j' to 0
    i = 1  # Initialize step 'i' to 1

    # Loop while step 'i' is less than or equal to 500000
    while i <= 500000:
        if is_true[j]:  # Check if 'is_true[j]' is True
            is_true[j] = False  # Mark the current position as False
        
        i += 1  # Increment step 'i' by 1
        j = (j + i) % n  # Update index 'j' to (j + i) MOD n

    # Create a list 'remaining_true' with elements from 'is_true' that are still True
    remaining_true = [value for value in is_true if value]

    # Check if the length of 'remaining_true' is equal to 0
    if len(remaining_true) == 0:
        print('YES')  # All positions have been marked False
    else:
        print('NO')  # There are still True values indicating some positions are unmarked
