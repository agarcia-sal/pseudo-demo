# Start of the program

# Read an integer value and assign it to n
n = int(input())

# Create a list of boolean values initialized to True, of size n
is_true = [True] * n

# Initialize variables j and i
j = 0
i = 1

# Loop until i exceeds 500000
while i <= 500000:
    # Check if the current index j in list is True
    if is_true[j]:
        # Set the current index j to False
        is_true[j] = False
    
    # Increment i by 1
    i += 1
    
    # Update j using modulo n to wrap around the index
    j = (j + i) % n

# Create a new list containing all elements in is_true that are True
active_indices = [value for value in is_true if value]

# Check if the length of active_indices is 0
if len(active_indices) == 0:
    print('YES')
else:
    print('NO')

# End of the program
