def CheckBooleanArray(n):
    # Initialize a boolean array 'b' of size n, all set to True
    b = [True] * n
    
    # Initialize variables for the loop
    j = 0
    i = 1

    # Loop continues until i exceeds 500000
    while i <= 500000:
        # If the current index j in array b is True, set it to False
        if b[j]:
            b[j] = False
            
        # Increment i
        i += 1
        
        # Update j using modulus operation to stay within the bounds of the array
        j = (j + i) % n

    # Create a list x containing all True values from b
    x = [value for value in b if value]
    
    # Check the length of x to determine the output
    if len(x) == 0:
        print('YES')  # Output if no True values remain
    else:
        print('NO')   # Output if there are still True values

# Example of reading an integer input for the function
n = int(input())
CheckBooleanArray(n)
