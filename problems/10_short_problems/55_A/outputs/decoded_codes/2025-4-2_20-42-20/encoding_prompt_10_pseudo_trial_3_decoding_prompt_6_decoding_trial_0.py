# Step 1: Read an integer from user input
number_of_elements = int(input())

# Step 2: Initialize a list 'b' with 'number_of_elements' elements, all set to True
boolean_list = [True] * number_of_elements

# Step 3: Initialize variables
current_index = 0  # current index in the list
step_counter = 1    # step counter

# Step 4: Loop until step_counter exceeds 500000
while step_counter <= 500000:
    
    # Step 5: Check if the current index in list 'b' is True
    if boolean_list[current_index]:
        # Step 6: Set the current index to False
        boolean_list[current_index] = False
        
    # Step 7: Increment step_counter by 1
    step_counter += 1
    
    # Step 8: Update current_index to wrap around within bounds of 'number_of_elements'
    current_index = (current_index + step_counter) % number_of_elements

# Step 9: Create a list 'x' of elements in 'b' that are still True
true_elements = [value for value in boolean_list if value]

# Step 10: Check the length of list 'true_elements'
if len(true_elements) == 0:
    print('YES')
else:
    print('NO')
