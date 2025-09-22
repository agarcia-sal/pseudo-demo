# Start of the program

# Define integer variable n and read input value
n = int(input())

# Create a list b of size n, initializing all elements to True
b = [True] * n

# Initialize integer variable j to 0
j = 0

# Initialize integer variable i to 1
i = 1

# While i is less than or equal to 500000
while i <= 500000:
    # If b[j] is True
    if b[j]:
        # Set b[j] to False
        b[j] = False
    
    # Increment i by 1
    i += 1
    
    # Update j by calculating (j + i) modulo n
    j = (j + i) % n

# Create a new list x that contains all elements in b that are True
x = [value for value in b if value]

# If the length of x is 0
if len(x) == 0:
    # Print 'YES'
    print('YES')
else:
    # Print 'NO'
    print('NO')

# End of the program
