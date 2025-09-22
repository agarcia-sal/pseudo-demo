# Step 1: Input the number n
n = int(input())

# Step 2: Initialize a list b with TRUE values
b = [True] * n  # Create a list of size n filled with True

# Step 3: Initialize loop control variables
j = 0
i = 1

# Step 4: Main loop to update the list b
while i <= 500000:
    # Step 5: Check if current position j is marked TRUE
    if b[j]:
        b[j] = False  # Mark the position j as FALSE

    # Step 6: Increment i and update j for the next iteration
    i += 1
    j = (j + i) % n  # Update j with modular arithmetic for circular indexing

# Step 7: Create a list x with all TRUE values from list b
x = [b_elem for b_elem in b if b_elem]  # List comprehension to filter TRUE values

# Step 8: Check if list x is empty
if len(x) == 0:
    print('YES')  # Print 'YES' if no TRUE values are left
else:
    print('NO')  # Print 'NO' if there are still TRUE values left
