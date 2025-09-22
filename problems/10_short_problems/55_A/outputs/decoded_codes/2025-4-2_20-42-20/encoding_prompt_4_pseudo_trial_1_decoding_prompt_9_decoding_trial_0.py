# Step 1: Get user input for the size of the list
n = int(input())

# Step 2: Create a list b of size n initialized with True values
b = [True] * n

# Step 3: Initialize j and i
j = 0
i = 1

# Step 4: While loop to mark elements
while i <= 500000:
    if b[j]:  # Check if the current index is True
        b[j] = False  # Mark the current index as False
    i += 1  # Increment i
    j = (j + i) % n  # Update index for the next iteration

# Step 5: Create a list x containing all values from b that are True
x = [value for value in b if value]

# Step 6: Check the length of x and print the result
if len(x) == 0:
    print('YES')  # All elements were marked False
else:
    print('NO')   # There are still True elements in the list
