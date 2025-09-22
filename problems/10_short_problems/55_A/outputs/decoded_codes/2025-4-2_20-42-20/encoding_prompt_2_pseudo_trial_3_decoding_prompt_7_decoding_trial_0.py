# Start the program
# Step 2: Read number of elements from user input
number_of_elements = int(input())

# Step 3: Create a list called 'boolean_list' initialized to True
boolean_list = [True] * number_of_elements

# Step 4: Initialize position and increment
position = 0
increment = 1

# Step 5: Repeat while increment is less than or equal to 500,000
while increment <= 500000:
    # Step 5a: Check if the current entry in boolean_list at index position is True
    if boolean_list[position]:
        # If it is True, set that entry to False
        boolean_list[position] = False
    
    # Step 5b: Increase increment by 1
    increment += 1
    
    # Step 5c: Update position using modulus to stay within bounds
    position = (position + increment) % number_of_elements

# Step 6: Create a list of remaining True values
remaining_true_values = [val for val in boolean_list if val]

# Step 7: Check if any True values are left
if len(remaining_true_values) == 0:
    # Step 7a: If no True values, output 'YES'
    print('YES')
else:
    # Step 8: Otherwise, output 'NO'
    print('NO')

# End of the program
