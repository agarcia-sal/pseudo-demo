# Begin of the main code
# Read input value for n
n = int(input())

# Initialize a list of boolean values, all set to True
b = [True] * n

j = 0  # Initialize the index j
i = 1  # Initialize the increment i

# Loop until i exceeds 500000
while i <= 500000:
    # If the current position in the list is True
    if b[j]:
        # Mark the position as False
        b[j] = False
        
    # Increment i
    i += 1
    
    # Update the index j in a circular manner
    j = (j + i) % n

# Create a list x containing all elements from b that are True
x = [value for value in b if value]

# Check if there are any True values remaining
if len(x) == 0:
    print('YES')
else:
    print('NO')
