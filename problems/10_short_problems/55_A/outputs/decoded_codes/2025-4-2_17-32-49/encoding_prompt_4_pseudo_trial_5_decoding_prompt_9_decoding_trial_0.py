# Read an integer input for the size of the list
n = int(input())

# Initialize a boolean list with size n, all set to True
b = [True] * n

# Initialize starting indices
j = 0
i = 1

# Loop until i exceeds 500000
while i <= 500000:
    
    # If the current position in list b is True
    if b[j]:
        # Mark that position as False
        b[j] = False
    
    # Increment i
    i += 1
    
    # Update j using the formula and wrapping around with modulo
    j = (j + i) % n 

# Create a list x containing positions in b that are still True
x = [value for value in b if value]

# Check if list x is empty
if len(x) == 0:
    print('YES')  # No True values found
else:
    print('NO')   # There are some True values found
