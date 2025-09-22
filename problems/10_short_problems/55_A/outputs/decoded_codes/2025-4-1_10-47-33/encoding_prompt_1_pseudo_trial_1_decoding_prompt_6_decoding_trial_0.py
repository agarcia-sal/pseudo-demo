# Step 1: Get user input for the number of elements
number_of_elements = int(input())

# Step 2: Create a list of boolean values, all initialized to True
is_included = [True] * number_of_elements

# Step 3: Initialize the current index
current_index = 0

# Step 4: Initialize the increment value
increment = 1

# Step 5: Loop until increment exceeds 500000
while increment <= 500000:
    # If the current index in is_included is True, set it to False
    if is_included[current_index]:
        is_included[current_index] = False
    
    # Increment the increment value
    increment += 1
    
    # Update the current index using modulo operation
    current_index = (current_index + increment) % number_of_elements

# Step 6: Create a list of True values by filtering is_included list
true_values = [value for value in is_included if value]

# Step 7: Check the length of true_values and print output
if len(true_values) == 0:
    print("YES")
else:
    print("NO")
