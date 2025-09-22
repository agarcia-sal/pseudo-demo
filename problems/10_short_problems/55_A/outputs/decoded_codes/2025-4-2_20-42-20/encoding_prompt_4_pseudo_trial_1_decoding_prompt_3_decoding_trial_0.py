# Get user input for the size of the list
n = int(input())

# Initialize a list of size n with all values set to True
b = [True] * n

# Initialize variables for loop control
j = 0
i = 1

# Main loop to mark elements in the list
while i <= 500000:
    if b[j]:  # If current index is True
        b[j] = False  # Mark it as False
    i += 1  # Increment i
    j = (j + i) % n  # Update j using modulo to wrap around

# Create a list of all values in b that are still True
x = [value for value in b if value]

# Check if there are any True values left
if len(x) == 0:
    print('YES')  # All elements were marked False
else:
    print('NO')   # There are still True elements in the list
