# Step 1: Initialize variable
n = int(input())  # Read the integer input from the user

# Step 2: Create a list 'b' of Boolean values initialized to True
b = [True] * n  # A list of True values with length n

# Step 3: Initialize counters
j = 0
i = 1

# Step 4: Loop while 'i' is less than or equal to 500000
while i <= 500000:
    # Step 5: Check if the current position 'j' is still True
    if b[j]:
        b[j] = False  # Mark the position as False

    # Increment 'i' and update 'j' for the next iteration
    i += 1
    j = (j + i) % n  # Update 'j' using modular arithmetic

# Step 6: Create list 'x' to store positions in 'b' that are still True
x = [val for val in b if val]  # List of elements in 'b' that are still True

# Step 7: Check the length of 'x'
if len(x) == 0:
    print('YES')  # All values have been marked False
else:
    print('NO')  # There are still True values in 'b'
