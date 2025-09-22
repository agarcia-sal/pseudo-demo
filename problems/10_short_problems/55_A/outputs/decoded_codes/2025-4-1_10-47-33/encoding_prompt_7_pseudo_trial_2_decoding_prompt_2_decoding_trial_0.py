def checkStatusOfElements(n):
    # Initialize array 'b' of size n with all values set to True
    b = [True] * n
    j = 0  # Set index 'j' to 0
    i = 1  # Set counter 'i' to 1

    # Loop until counter 'i' is greater than 500000
    while i <= 500000:
        # If element at index 'j' in array 'b' is True
        if b[j]:
            # Set element at index 'j' in array 'b' to False
            b[j] = False
        
        # Increment counter 'i' by 1
        i += 1
        
        # Update index 'j' to (index 'j' + counter 'i') modulo n
        j = (j + i) % n

    # Create a new array 'x' containing all True values from array 'b'
    x = [value for value in b if value]

    # Check the length of array 'x'
    if len(x) == 0:
        print("YES")  # Indicates that all elements in 'b' have been set to False
    else:
        print("NO")   # Indicates that there are still True elements in 'b'

# Example Usage:
n = int(input())
checkStatusOfElements(n)
