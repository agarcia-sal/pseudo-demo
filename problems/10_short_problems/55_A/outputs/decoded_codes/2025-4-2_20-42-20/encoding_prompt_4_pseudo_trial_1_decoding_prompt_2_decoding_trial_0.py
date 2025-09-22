# Step 1: Read input from user
n = int(input())

# Step 2: Initialize a list `b` of size `n` with all values set to True
b = [True] * n

# Step 3: Initialize counters
j = 0
i = 1

# Step 4: Perform the main operation loop
while i <= 500000:
    if b[j]:  # Check if current index `j` is True
        b[j] = False  # Mark current index as False
    i += 1  # Increment `i` by 1
    j = (j + i) % n  # Update index `j` for the next iteration

# Step 5: Create a list `x` containing all True values from list `b`
x = [value for value in b if value]

# Step 6: Check the length of `x` and print the appropriate message
if len(x) == 0:
    print('YES')  # All elements were marked as False
else:
    print('NO')   # There are still True elements in the list
