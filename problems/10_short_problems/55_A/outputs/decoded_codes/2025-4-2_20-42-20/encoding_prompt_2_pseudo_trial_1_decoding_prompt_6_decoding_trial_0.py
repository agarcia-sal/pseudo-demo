# Start the program.
# Step 2: Get an integer input from the user
number_of_elements = int(input())

# Step 3: Create a list initialized to True
is_available = [True] * number_of_elements

# Step 4: Initialize index and increment variables
index = 0
increment = 1

# Step 6: While increment is less than or equal to 500000
while increment <= 500000:
    # Check if the element at is_available[index] is True
    if is_available[index]:
        # If it is True, set it to False
        is_available[index] = False
    
    # Increase increment by 1
    increment += 1
    
    # Update index to be (index + increment) mod number_of_elements
    index = (index + increment) % number_of_elements

# Step 7: Create a list of remaining True elements
remaining_true = [element for element in is_available if element]

# Step 8: Check the length of remaining_true
if len(remaining_true) == 0:
    # If it's 0, output 'YES'
    print('YES')
else:
    # Otherwise, output 'NO'
    print('NO')

# End the program.
