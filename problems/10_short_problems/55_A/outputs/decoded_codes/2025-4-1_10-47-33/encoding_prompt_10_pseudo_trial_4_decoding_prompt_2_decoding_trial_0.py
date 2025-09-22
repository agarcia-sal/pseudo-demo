# Step 1: Input Handling
n = int(input())

# Step 2: Initialize a boolean list b
b = [True] * n  # List of size n initialized with True values
j = 0
i = 1

# Step 3: Loop to modify the boolean list
while i <= 500000:
    if b[j]:  # If b[j] is True
        b[j] = False  # Set b[j] to False

    # Step 4: Increment i and update j
    i += 1
    j = (j + i) % n  # Update j

# Step 5: Extract remaining TRUE values from b
x = [value for value in b if value]  # List containing elements from b where value is True

# Step 6: Check the result and print output
if len(x) == 0:
    print('YES')
else:
    print('NO')
