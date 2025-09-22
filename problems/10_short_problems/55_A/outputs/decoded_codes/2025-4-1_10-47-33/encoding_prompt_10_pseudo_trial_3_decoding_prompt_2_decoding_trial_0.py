# Step 1: Input the size of the array
n = int(input())  # Read an integer value for the size of the array

# Step 2: Initialize an array (list) with True values
b = [True] * n  # Create a list 'b' of size n, initialized with True values

# Step 3: Initialize variables for looping
j = 0
i = 1

# Step 4: Loop to process values while i is less than or equal to 500000
while i <= 500000:
    # If the current position j in the list b is True
    if b[j]:
        b[j] = False  # Mark position j as False
    
    i += 1  # Increment i to move to the next value
    j = (j + i) % n  # Update position j using modulo to wrap around

# Step 5: Create a new list x containing only True values from b
x = [a for a in b if a]  # Generate a list 'x' with elements from 'b' that are True

# Step 6: Check if the list x is empty and print the result
if len(x) == 0:
    print("YES")  # No True values left in b
else:
    print("NO")   # There are still True values in b
