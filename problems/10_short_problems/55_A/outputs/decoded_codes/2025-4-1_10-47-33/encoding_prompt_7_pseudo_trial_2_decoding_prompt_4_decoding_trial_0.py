def check_status_of_elements(n):
    # Initialize an array 'b' of size n with all values set to True
    b = [True] * n
    j = 0  # Initialize index j
    i = 1  # Initialize counter i

    # Loop until counter i is less than or equal to 500000
    while i <= 500000:
        if b[j]:  # Check if the element at index j is True
            b[j] = False  # Set the element at index j to False
        
        i += 1  # Increment counter i
        j = (j + i) % n  # Update index j using modulo n for wrapping around
    
    # Create a new array 'x' containing all True values from array 'b'
    x = [value for value in b if value]

    # Output results based on the contents of array 'x'
    if len(x) == 0:
        print('YES')  # All elements in b have been set to False
    else:
        print('NO')   # There are still True elements in b

# Example usage:
n = int(input())
check_status_of_elements(n)
