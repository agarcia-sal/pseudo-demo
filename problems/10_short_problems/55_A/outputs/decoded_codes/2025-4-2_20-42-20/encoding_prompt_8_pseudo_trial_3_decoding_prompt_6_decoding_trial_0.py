# Step 1: Get the total number of boolean elements from the user
number_of_booleans = int(input())

# Step 2: Create a list of booleans, all initialized to True
boolean_list = [True] * number_of_booleans

# Step 3: Initialize the current index and the increment
current_index = 0
increment = 1

# Step 4: Set a limit for the incrementing loop
limit = 500000

# Step 5: Update loop to modify the boolean list
while increment <= limit:
    # If the current index in boolean list is True
    if boolean_list[current_index]:
        boolean_list[current_index] = False  # Set it to False
    
    increment += 1  # Increase increment by 1
    
    # Update current index using the increment and take modulo to wrap around
    current_index = (current_index + increment) % number_of_booleans

# Step 6: Collect remaining True values from boolean_list
remaining_true = [value for value in boolean_list if value]

# Step 7: Output result based on the length of remaining_true
if len(remaining_true) == 0:
    print('YES')  # All values are False
else:
    print('NO')   # At least one value is True
