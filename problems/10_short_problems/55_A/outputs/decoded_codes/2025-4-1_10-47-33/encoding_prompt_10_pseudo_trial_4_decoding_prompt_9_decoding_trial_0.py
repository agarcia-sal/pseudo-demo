# Step 1: Input Handling
n = int(input())  # Read an integer input

# Step 2: Initialize a boolean list 'b'
b = [True] * n  # List of boolean with size n initialized to True
j = 0  # Initialize index j
i = 1  # Initialize index i

# Step 3: Loop to modify the boolean list
while i <= 500000:  # Continue until i exceeds 500000
    if b[j]:  # If the current index in b is True
        b[j] = False  # Set the current index to False
    
    # Step 4: Increment i and update j
    i += 1  # Increment i
    j = (j + i) % n  # Update j to wrap around using modulo

# Step 5: Extract remaining True values from b
x = [value for value in b if value]  # Filter to get True values from b

# Step 6: Check the result and print output
if len(x) == 0:  # If there are no True values left
    print('YES')  # Print 'YES' if the list is empty
else:
    print('NO')  # Print 'NO' if there are remaining True values
