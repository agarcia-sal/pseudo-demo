# Read a positive integer input for the size of the array
n = int(input())

# Initialize a boolean array of size n, all elements set to True
b = [True] * n

# Initialize variables
j = 0  # This will track the index in the array
i = 1  # This will be incremented in the loop

# Loop while i is less than or equal to 500000
while i <= 500000:
    # If the current index in array b is True
    if b[j]:
        # Set the current index in array b to False
        b[j] = False
    
    # Increment i by 1
    i += 1
    
    # Update j to the next index using the formula
    j = (j + i) % n

# Create a list x that contains all True values from array b
x = [element for element in b if element]

# Check the length of the list x
if len(x) == 0:
    # If x is empty, output 'YES'
    print('YES')
else:
    # If x is not empty, output 'NO'
    print('NO')
