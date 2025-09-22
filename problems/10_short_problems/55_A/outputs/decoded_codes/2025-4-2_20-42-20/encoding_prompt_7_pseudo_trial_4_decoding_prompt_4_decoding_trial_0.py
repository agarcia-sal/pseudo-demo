def check_consecutive_numbers(n):
    # Initialize an array 'is_true' of size n with all values set to True
    is_true = [True] * n
    j = 0  # Initialize index 'j' to 0
    i = 1  # Initialize step 'i' to 1

    # Loop until 'i' exceeds 500,000
    while i <= 500000:
        if is_true[j]:  # Check if current position is True
            is_true[j] = False  # Mark the current position as False
        
        j = (j + i) % n  # Update index 'j' using modular arithmetic
        i += 1  # Increment step 'i' by 1

    # Create a list of remaining True values
    remaining_true = [value for value in is_true if value]

    # Check for remaining True values and print result
    if len(remaining_true) == 0:
        print('YES')  # All positions have been marked False
    else:
        print('NO')   # Some positions are still True

# Example of how to use the function
n = int(input())  # Read input value for n
check_consecutive_numbers(n)
