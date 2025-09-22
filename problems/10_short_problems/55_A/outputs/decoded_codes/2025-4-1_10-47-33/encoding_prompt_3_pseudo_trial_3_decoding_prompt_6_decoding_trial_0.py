# Input
n = int(input())  # Get an integer value 'n' from user input

# Initialize a boolean list 'isActive' of size n
is_active = [True] * n  # Set isActive to a list of size n filled with True
index = 0  # Set initial index
increment = 1  # Set initial increment

# Process to modify the 'isActive' list
while increment <= 500000:  # While increment is less than or equal to 500000
    if is_active[index]:  # If isActive at index is True
        is_active[index] = False  # Mark isActive at index as False
    
    # Update increment and index for the next iteration
    increment += 1  # Increment by 1
    index = (index + increment) % n  # Update index using modulo n

# Create a new list 'activeElements' from the 'isActive' list
active_elements = [element for element in is_active if element]  # List of all True values from isActive

# Output Result
if len(active_elements) == 0:  # If the size of activeElements is 0
    print('YES')  # Indicating all elements are marked False
else:
    print('NO')  # Indicating there are still True elements present
