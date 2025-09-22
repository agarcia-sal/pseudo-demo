# Read an integer value 'n' as input
n = int(input())  # Assuming input is provided as an integer

# Create a list 'b' and populate it with True values
b = [True] * n  # Initializes a list of size n with all elements set to True

# Initialize variables for the algorithm
j = 0
i = 1

# Start a loop that continues while i is less than or equal to 500000
while i <= 500000:
    # Check if the current position in the list 'b' is True
    if b[j] is True:
        # Set the current position in the list to False
        b[j] = False
    
    # Increment the counter i
    i += 1
    
    # Update the index j using a formula based on the current i
    j = (j + i) % n

# Create a new list 'x' to hold the values that are still True in list 'b'
x = [value for value in b if value is True]  # List comprehension to filter True values

# Check the length of the list 'x'
if len(x) == 0:
    # If there are no True values left, print "YES"
    print('YES')
else:
    # If there are still True values left, print "NO"
    print('NO')
