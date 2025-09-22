def checkStatusOfElements(n):
    # Initialize array 'b' of size n with all values set to True
    b = [True] * n
    j = 0
    i = 1
    
    # Loop until counter i exceeds 500000
    while i <= 500000:
        if b[j]:  # Check if the element at index 'j' in 'b' is True
            b[j] = False  # Set element at index 'j' in 'b' to False
        i += 1  # Increment counter i by 1
        j = (j + i) % n  # Update index 'j'
    
    # Create a new array 'x' containing all True values from 'b'
    x = [value for value in b if value]
    
    # Check if 'x' is empty and print the result
    if len(x) == 0:
        print('YES')  # All elements in 'b' have been set to False
    else:
        print('NO')   # There are still True elements in 'b'

# Example usage
n = int(input())
checkStatusOfElements(n)
