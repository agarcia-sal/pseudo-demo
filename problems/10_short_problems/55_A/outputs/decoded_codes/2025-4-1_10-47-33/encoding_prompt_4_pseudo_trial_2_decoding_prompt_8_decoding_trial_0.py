# Read an integer input representing the number of elements
n = int(input())

# Create a list 'b' initialized with 'True' values to track state
b = [True] * n

# Initialize counters
j = 0  # Index for the list
i = 1  # Counter for iterations

# Loop while i is less than or equal to 500000
while i <= 500000:
    # If the current index j in list b is True
    if b[j]:
        # Set that index to False
        b[j] = False

    # Increment i by 1
    i += 1

    # Update index j with wrapping around using modulus operator
    j = (j + i) % n

# Create a list 'x' containing all True values from list 'b'
x = [value for value in b if value]

# Check if the list 'x' is empty
if len(x) == 0:
    print('YES')  # Output if there are no True values
else:
    print('NO')   # Output if there are any True values
