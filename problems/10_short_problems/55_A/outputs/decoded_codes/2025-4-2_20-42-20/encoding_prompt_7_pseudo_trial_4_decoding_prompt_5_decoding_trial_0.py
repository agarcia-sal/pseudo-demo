def check_consecutive_numbers(n):
    # Initialize an array 'is_true' of size n with all values set to True
    is_true = [True] * n
    j = 0  # Index for position tracking
    i = 1  # Step increment

    # Loop until the step 'i' exceeds 500,000
    while i <= 500000:
        if is_true[j]:  # Check if the current position is True
            is_true[j] = False  # Mark the current position as False

        # Increment step 'i'
        i += 1
        j = (j + i) % n  # Update index 'j' using modular arithmetic

    # Create a list of remaining True values
    remaining_true = [value for value in is_true if value]

    # Check if any positions remain True
    if len(remaining_true) == 0:
        print('YES')  # All positions have been marked False
    else:
        print('NO')  # Some positions are still True

# Example of how to call the function:
# n = int(input())
# check_consecutive_numbers(n)
