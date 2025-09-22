# Read an integer value n from the user
n = int(input())

# Initialize a list of boolean values, all set to True, representing active status
is_active = [True] * n

# Initialize the variables
current_index = 0
increment = 1

# Loop until increment exceeds 500,000
while increment <= 500000:
    # If the current index in is_active is True, set it to False
    if is_active[current_index]:
        is_active[current_index] = False
    
    # Increment the currentIndex by the value of increment and use modulo to wrap around
    current_index = (current_index + increment) % n
    
    # Increment the increment value for the next iteration
    increment += 1

# Create a new list that contains only the True values from is_active
active_count = sum(is_active)  # Count of True values in is_active

# If no active items are found, print 'YES', otherwise print 'NO'
if active_count == 0:
    print('YES')
else:
    print('NO')
