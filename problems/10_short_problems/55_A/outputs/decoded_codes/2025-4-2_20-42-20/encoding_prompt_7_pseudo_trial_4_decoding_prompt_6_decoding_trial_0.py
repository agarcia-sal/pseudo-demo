def check_consecutive_numbers(n):
    # Initialize an array 'is_true' of size n with all values set to True
    is_true = [True] * n
    j = 0  # Initialize index 'j' to 0
    i = 1  # Initialize step 'i' to 1

    # Loop until step 'i' reaches 500,000
    while i <= 500000:
        # If the current position is True, set it to False
        if is_true[j]:
            is_true[j] = False
        # Increment step 'i'
        i += 1
        # Update the index 'j'
        j = (j + i) % n  # Move to the next index based on the current step

    # Collect remaining True values from 'is_true'
    remaining_true = [value for value in is_true if value]

    # Check the length of 'remaining_true'
    if len(remaining_true) == 0:
        print('YES')  # All positions have been marked False
    else:
        print('NO')   # There are still True values indicating some positions are unmarked

# Example of how to call the function
n = int(input())  # Read an integer input from the user
check_consecutive_numbers(n)
