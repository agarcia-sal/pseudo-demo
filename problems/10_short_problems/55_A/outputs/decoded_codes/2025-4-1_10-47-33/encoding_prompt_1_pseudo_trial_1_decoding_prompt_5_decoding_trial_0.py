# Request user to input the number of elements
number_of_elements = int(input())

# Create a list of boolean values initialized to True
is_included = [True] * number_of_elements

# Initialize current index and increment values
current_index = 0
increment = 1

# Loop to modify the is_included list
while increment <= 500000:
    if is_included[current_index]:
        is_included[current_index] = False  # Mark the current index as False
    increment += 1  # Increment the counter
    current_index = (current_index + increment) % number_of_elements  # Update the index

# Create a list of indices that are still True
true_values = [value for value in is_included if value]

# Check if there are any remaining True values
if len(true_values) == 0:
    print("YES")  # Output "YES" if all indices are False
else:
    print("NO")   # Output "NO" otherwise
