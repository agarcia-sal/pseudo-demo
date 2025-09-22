# Initialize the number of elements based on user input
number_of_elements = int(input())
# Create a list of boolean values initialized to True
is_included = [True] * number_of_elements

# Initialize the current index and increment
current_index = 0
increment = 1

# While increment is less than or equal to 500000
while increment <= 500000:
    # If the value at the current index is True, set it to False
    if is_included[current_index]:
        is_included[current_index] = False
    # Increment the increment variable
    increment += 1
    # Update the current index using modulo operation
    current_index = (current_index + increment) % number_of_elements

# Create a list of values that are still True
true_values = [value for value in is_included if value]

# Output result based on the length of true values
if len(true_values) == 0:
    print("YES")
else:
    print("NO")
