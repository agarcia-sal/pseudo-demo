# Begin the program

# Read an integer input representing the size
size = int(input())

# Create a boolean list initialized to True for all indices
bool_list = [True] * size

# Initialize index variables
current_index = 0
step_size = 1

# Loop until step_size exceeds 500,000
while step_size <= 500000:
    
    # If the current position in the boolean list is True
    if bool_list[current_index]:
        # Set the current position to False
        bool_list[current_index] = False
    
    # Increment the step_size
    step_size += 1

    # Update the current_index with the new position
    current_index = (current_index + step_size) % size

# Create a new list containing all True values from the boolean list
true_values = [value for value in bool_list if value]

# Check if there are any True values left
if len(true_values) == 0:
    # If no True values are found, print 'YES'
    print('YES')
else:
    # If there are True values, print 'NO'
    print('NO')
