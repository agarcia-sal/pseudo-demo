# Getting the number of elements from the user
number_of_elements = int(input())

# Initialize a list to track inclusion status of each index
is_included = [True] * number_of_elements

# Initialize current index and increment variables
current_index = 0
increment = 1

# Process to mark indices as False
while increment <= 500000:
    if is_included[current_index]:
        is_included[current_index] = False
    
    increment += 1
    current_index = (current_index + increment) % number_of_elements

# Create a list of the indices that are still included (True)
true_values = [value for value in is_included if value]

# Check the length of true_values to determine the output
if len(true_values) == 0:
    print("YES")
else:
    print("NO")
