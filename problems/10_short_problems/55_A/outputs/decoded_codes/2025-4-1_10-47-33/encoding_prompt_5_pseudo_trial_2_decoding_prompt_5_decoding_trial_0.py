# Start of the program to simulate the elimination process
n = int(input())  # Get the size of the list from user input

# Initialize a list with all elements set to True
boolean_list = [True] * n

# Set up counters for the elimination process
outer_counter = 1
inner_counter = 0

# Elimination loop that runs up to 500000 iterations
while outer_counter <= 500000:
    # Check if current element is True
    if boolean_list[inner_counter]:
        # Eliminating the element by setting it to False
        boolean_list[inner_counter] = False
        
    # Increment the outer counter
    outer_counter += 1
    
    # Update inner counter to new position within bounds of the list
    inner_counter = (inner_counter + outer_counter) % n

# Create a list of remaining True values
remaining_true_values = [value for value in boolean_list if value]

# Determine the result based on the remaining values
if len(remaining_true_values) == 0:
    print('YES')  # Output if all values have been eliminated
else:
    print('NO')   # Output if there are still True values left
