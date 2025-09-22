# Start of the Program

# Get the size of the list from the user input
size_of_list = int(input())

# Initialize a list named booleanList with 'size_of_list' elements, all set to True
boolean_list = [True] * size_of_list

# Initialize counters
outer_counter = 1
inner_counter = 0

# Elimination Loop
while outer_counter <= 500000:
    # Check if the current element at inner_counter is True
    if boolean_list[inner_counter]:
        # Set that element to False (indicating elimination)
        boolean_list[inner_counter] = False
    
    # Increase outerCounter by 1
    outer_counter += 1
    
    # Update innerCounter by adding outerCounter and taking modulo by size_of_list
    inner_counter = (inner_counter + outer_counter) % size_of_list

# Create a new list of remaining True values
remaining_true_values = [value for value in boolean_list if value]

# Determine result based on remaining true values
if len(remaining_true_values) == 0:
    # Output 'YES' if all values have been eliminated
    print('YES')
else:
    # Output 'NO' if some values are still True
    print('NO')
