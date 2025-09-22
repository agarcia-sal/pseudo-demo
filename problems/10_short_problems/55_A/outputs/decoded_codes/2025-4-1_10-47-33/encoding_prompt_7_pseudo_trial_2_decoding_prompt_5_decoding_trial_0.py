def check_status_of_elements(n):
    # Initialize an array 'b' of size n with all values set to True
    b = [True] * n
    j = 0  # Index to track position in the array
    counter = 1  # Counter starting from 1
    
    # Loop until counter is greater than 500000
    while counter <= 500000:
        if b[j]:  # If the current element is True
            b[j] = False  # Set it to False
        counter += 1  # Increment counter
        j = (j + counter) % n  # Update index j modulo n
    
    # Create a new array 'x' with all True values remaining in 'b'
    x = [value for value in b if value]
    
    # Check if array 'x' is empty
    if len(x) == 0:
        print('YES')  # All elements in 'b' are False
    else:
        print('NO')   # There are still True elements in 'b'

# Example test cases (uncomment to test):
# check_status_of_elements(10)
# check_status_of_elements(0)
