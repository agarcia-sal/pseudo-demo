# Start the program.
# Get an integer input from the user
number_of_elements = int(input())

# Create a list with number_of_elements initialized to True
is_available = [True] * number_of_elements

# Initialize the variables
index = 0
increment = 1

# Loop while increment is less than or equal to 500000
while increment <= 500000:
    # Check if the element at is_available[index] is True
    if is_available[index]:
        # Set it to False if it is True
        is_available[index] = False
    
    # Increase increment by 1
    increment += 1
    
    # Update index
    index = (index + increment) % number_of_elements

# Create a new list containing remaining true values
remaining_true = [value for value in is_available if value]

# Check the length of remaining_true
if len(remaining_true) == 0:
    print('YES')  # Output 'YES' if no elements are True
else:
    print('NO')   # Output 'NO' if there are still True elements
