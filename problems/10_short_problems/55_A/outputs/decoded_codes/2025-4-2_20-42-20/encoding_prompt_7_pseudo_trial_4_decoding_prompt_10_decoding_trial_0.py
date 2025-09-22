def check_consecutive_numbers(n):
    # Initialize an array of size n with all values set to True
    is_true = [True] * n
    j = 0  # Initialize index to 0
    i = 1  # Initialize step to 1

    # Loop until step i exceeds 500,000
    while i <= 500000:
        if is_true[j]:  # Check if the current position is still True
            is_true[j] = False  # Mark the position as False
        
        j = (j + i) % n  # Move to the next index based on the current step
        i += 1  # Increment the step

    # Create a list of remaining True values in is_true
    remaining_true = [value for value in is_true if value]

    # Check if there are any remaining True values and print the result
    if len(remaining_true) == 0:
        print('YES')  # All positions have been marked False
    else:
        print('NO')   # There are still True values indicating some positions are unmarked

# Example usage:
# Uncomment the following lines to test the function
# n = int(input())
# check_consecutive_numbers(n)
