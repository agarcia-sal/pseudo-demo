def check_status_of_elements(n):
    # Initialize array 'b' of size n with all values set to True
    b = [True] * n
    j = 0  # Initialize index 'j' to 0
    i = 1  # Initialize counter 'i' to 1
    
    # Loop until 'i' exceeds 500000
    while i <= 500000:
        # If current element in array 'b' is True, set it to False
        if b[j]:
            b[j] = False
        
        # Increment counter 'i' by 1
        i += 1
        
        # Update index 'j' to (j + i) modulo n
        j = (j + i) % n
    
    # Create a new array 'x' containing all True values from array 'b'
    x = [value for value in b if value]
    
    # Check if 'x' is empty
    if len(x) == 0:
        print('YES')  # All elements in 'b' have been set to False
    else:
        print('NO')   # There are still True elements in 'b'

# Example usage:
n = int(input())
check_status_of_elements(n)
