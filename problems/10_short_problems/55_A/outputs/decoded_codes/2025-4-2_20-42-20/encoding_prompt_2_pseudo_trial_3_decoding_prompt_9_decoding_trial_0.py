# Begin the program
# Read the number of elements from user input
number_of_elements = int(input())

# Create a list filled with True values
boolean_list = [True] * number_of_elements

# Initialize position and increment
position = 0
increment = 1

# Repeat the process while increment is less than or equal to 500,000
while increment <= 500000:
    # Check if the current entry in boolean_list at index position is True
    if boolean_list[position]:
        # Set that entry to False
        boolean_list[position] = False
    
    # Increase the increment by 1
    increment += 1
    
    # Update the position and wrap around using modulus
    position = (position + increment) % number_of_elements

# Create a new list with remaining True values
remaining_true_values = [value for value in boolean_list if value]

# Check if there are no remaining True values
if len(remaining_true_values) == 0:
    print('YES')
else:
    print('NO')
# End the program
