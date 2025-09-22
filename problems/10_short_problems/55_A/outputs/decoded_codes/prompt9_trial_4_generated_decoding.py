# Initialize Variables
number_of_elements = int(input())
boolean_array = [True] * number_of_elements  # Create a list filled with True
index = 0  # Track current position in boolean_array
increment = 1  # Initial increment value

# Loop Through a Sequence
while increment <= 500000:
    if boolean_array[index]:  # Check if the current position is True
        boolean_array[index] = False  # Mark this position as False
    increment += 1  # Increase increment
    index = (index + increment) % number_of_elements  # Update the index

# Check for True Values
remaining_true_values = [value for value in boolean_array if value]

# Output Result
if len(remaining_true_values) == 0:
    print("YES")  # All values were marked as False
else:
    print("NO")  # There are still True values in the list
