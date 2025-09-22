# Begin the program
# Get an integer input from the user, representing the total number of elements
total_elements = int(input())

# Create a list called boolean_list with a size of total_elements, initialized to True
boolean_list = [True] * total_elements

# Initialize current_index to 0 and increment to 1
current_index = 0
increment = 1

# Start a loop that continues while increment is less than or equal to 500,000
while increment <= 500000:
    # Check if the current position in boolean_list is True
    if boolean_list[current_index]:
        # Set that position in boolean_list to False
        boolean_list[current_index] = False
    
    # Increase increment by 1
    increment += 1
    
    # Update current_index using modulo total_elements to wrap around
    current_index = (current_index + increment) % total_elements

# Create a new list called remaining_true_values containing all elements from boolean_list that are still True
remaining_true_values = [value for value in boolean_list if value]

# Check the length of remaining_true_values
if len(remaining_true_values) == 0:
    # Output "YES" if there are no remaining True values
    print("YES")
else:
    # Output "NO" if there are remaining True values
    print("NO")
