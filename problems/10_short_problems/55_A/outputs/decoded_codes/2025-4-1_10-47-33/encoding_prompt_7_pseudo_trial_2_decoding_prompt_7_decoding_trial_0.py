def checkStatusOfElements(n):
    # Initialize the array 'b' with all values set to True
    b = [True] * n

    # Initialize the index 'j' and the counter 'i'
    j = 0
    i = 1
    
    # Perform the loop up to 500,000 iterations
    while i <= 500000:
        # If the current element is True, set it to False
        if b[j]:
            b[j] = False
        
        # Increment the counter 'i'
        i += 1
        
        # Update the index 'j', ensuring it wraps around using modulo
        j = (j + i) % n
    
    # Create a new array 'x' containing all True values from array 'b'
    x = [value for value in b if value]
    
    # Check the length of array 'x' to determine the output
    if len(x) == 0:
        print('YES')  # All elements have been set to False
    else:
        print('NO')   # There are still True elements in 'b'

# Example of calling the function
n = int(input())
checkStatusOfElements(n)
