# Step 1: Read input value for the number of elements
number_of_elements = int(input())

# Step 2: Initialize a list to track boolean values
boolean_list = [True] * number_of_elements

# Step 3: Initialize variables for iteration
index_to_change = 0
current_step = 1

# Step 4: Loop until the current step exceeds 500,000
while current_step <= 500000:
    # Step 5: Check if the current index has a True value
    if boolean_list[index_to_change]:
        # Step 6: Mark the current index as False
        boolean_list[index_to_change] = False
    
    # Step 7: Increment the current step counter
    current_step += 1
    
    # Step 8: Update the index_to_change using the current step value
    index_to_change = (index_to_change + current_step) % number_of_elements

# Step 9: Create a new list 'true_values' to hold all True values from boolean_list
true_values = [value for value in boolean_list if value]

# Step 10: Check if there are no True values in the true_values list
if len(true_values) == 0:
    print('YES')  # Output for the case when no True values are found
else:
    print('NO')   # Output for the case when there are True values found
