# Importing required library
from typing import List

# Step 1: Input the number n
n = int(input())  # Read an integer input

# Step 2: Initialize a list b with True values
b: List[bool] = [True] * n  # Create a list of size n, initialized to True

# Step 3: Initialize loop control variables
j = 0
i = 1

# Step 4: Main loop to update the list b
while i <= 500000:
    # Step 5: Check if current position j is marked True
    if b[j]:
        b[j] = False  # Mark the position as False

    # Step 6: Increment i and update j for the next iteration
    i += 1
    j = (j + i) % n  # Update j using modulo to wrap around

# Step 7: Create a list x with all True values from list b
x = [val for val in b if val]  # List comprehension to filter True values

# Step 8: Check if list x is empty
if len(x) == 0:
    print('YES')  # If x is empty, print 'YES'
else:
    print('NO')   # If x is not empty, print 'NO'
