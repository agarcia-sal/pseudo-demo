# Begin the program

# Step 1: Read input value for `n`
n = int(input())  # Read an integer value from user input

# Step 2: Initialize a list `b` with `n` True values
b = [True] * n  # Create a list of size n, initialized to True

# Step 3: Set initial indices for processing
j = 0  # Initialize index j
i = 1  # Initialize index i

# Step 4: Loop until `i` exceeds 500,000
while i <= 500000:  # Continue the loop as long as i is less than or equal to 500,000

    # Step 5: Check if the current position in list `b` is True
    if b[j]:  # If the current position in list b is True
        # Step 6: Mark the current position in list `b` as False
        b[j] = False  # Set the current position to False

    # Step 7: Increment the counter `i`
    i += 1  # Increment i by 1

    # Step 8: Update the index `j` for the next iteration
    j = (j + i) % n  # Update index circularly

# Step 9: Create a new list `x` containing only True values from `b`
x = [value for value in b if value]  # Create a list of all True values from b

# Step 10: Check if `x` is empty or not
if len(x) == 0:  # If the length of x is equal to 0
    print('YES')  # Output 'YES' indicating all positions are False
else:
    print('NO')   # Output 'NO' indicating there are still True values present
