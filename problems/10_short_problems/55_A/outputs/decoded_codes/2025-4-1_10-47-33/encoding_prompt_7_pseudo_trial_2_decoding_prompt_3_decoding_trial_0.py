def check_status_of_elements(n):
    # Initialize an array 'b' of size n with all values set to True
    b = [True] * n
    j = 0  # Index initialization
    i = 1  # Counter initialization

    # Loop until the counter 'i' exceeds 500000
    while i <= 500000:
        if b[j]:  # Check if the current element is True
            b[j] = False  # Set the current element to False
        i += 1  # Increment the counter
        j = (j + i) % n  # Update the index using modulo n

    # Create a new array 'x' containing all True values from array 'b'
    x = [value for value in b if value]

    # Check if there are any remaining True values in 'b'
    if len(x) == 0:
        print('YES')  # All elements in 'b' have been set to False
    else:
        print('NO')   # There are still True elements in 'b'

# Example usage
n = int(input())  # User inputs the size of the array
check_status_of_elements(n)
