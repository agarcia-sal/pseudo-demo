# Read an integer input from the user
n = int(input())
# Initialize a list b of size n with True values
b = [True] * n
# Initialize indices
j = 0
i = 1

# Loop until i exceeds 500000
while i <= 500000:
    # Mark the current index as False if it's within bounds
    if j < n:
        b[j] = False  # Mark the current index as False
    # Increment i
    i += 1
    # Update j to the next index using modulo
    j = (j + i) % n  # Update index for the next iteration

# Create a list x of all True values from b
x = [value for value in b if value]

# Check the length of x
if len(x) == 0:
    print('YES')  # All elements were marked False
else:
    print('NO')   # There are still True elements in the list
