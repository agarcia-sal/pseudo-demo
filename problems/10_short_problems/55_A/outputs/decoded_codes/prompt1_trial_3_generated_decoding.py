# Step 1
# Step 2
n = int(input())  # Read an integer value `n` from input.

# Step 3
b = [True] * n  # Initialize a list `b` of size `n`, with all elements set to `True`.

# Step 4
j = 0  # Set the index `j` to 0.

# Step 5
i = 1  # Set the counter `i` to 1.

# Step 6
while i <= 500000:  # While `i` is less than or equal to 500000 do:
    # Step 6a
    if b[j]:  # If the value at index `j` in list `b` is `True`:
        # Step 7
        b[j] = False  # Set the value at index `j` in list `b` to `False`.
    
    # Step 8
    i += 1  # Increment `i` by 1.
    
    # Step 9
    j = (j + i) % n  # Update index `j` to be the result of `(j + i) modulo n`.

# Step 10
x = [value for value in b if value]  # Create a new list `x` that contains all the elements from `b` that are still `True`.

# Step 11
if len(x) == 0:  # If the length of `x` is 0:
    # Step 12
    print('YES')  # Print 'YES'.
else:  # Otherwise:
    # Step 13
    print('NO')  # Print 'NO'.
