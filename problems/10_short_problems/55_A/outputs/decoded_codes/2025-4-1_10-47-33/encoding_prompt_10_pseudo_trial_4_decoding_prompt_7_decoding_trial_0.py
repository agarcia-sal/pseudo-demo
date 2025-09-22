# BEGIN

# Step 1: Input Handling
n = int(input())  # Read an integer input for size of the boolean list

# Step 2: Initialize a boolean list b
b = [True] * n  # Create a list of size n with all elements set to True
j = 0
i = 1

# Step 3: Loop to modify the boolean list
while i <= 500000:  # Continue until i exceeds 500000
    if b[j]:  # If the current index j is True
        b[j] = False  # Mark the position as False
        
    # Step 4: Increment i and update j
    i += 1  # Increment i by 1
    j = (j + i) % n  # Update j with modulo n to stay within bounds of list b

# Step 5: Extract remaining TRUE values from b
x = [value for value in b if value]  # Create a list containing only True values from b

# Step 6: Check the result and print output
if len(x) == 0:  # Check if the list x is empty
    print('YES')  # Print 'YES' if no True values remain
else:
    print('NO')  # Print 'NO' otherwise

# END
