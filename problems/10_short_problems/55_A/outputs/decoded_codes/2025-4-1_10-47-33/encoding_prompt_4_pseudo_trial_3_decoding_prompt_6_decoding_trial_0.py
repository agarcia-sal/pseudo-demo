# Start of the program
# Read a positive integer input for the size of the array
array_size = int(input())

# Initialize a boolean array of size array_size, all elements set to True
boolean_array = [True] * array_size

# Initialize variables
index_j = 0  # This will track the index in the array
increment_i = 1  # This will be incremented in the loop

# Loop while increment_i is less than or equal to 500000
while increment_i <= 500000:
    # If the current index in boolean_array is True
    if boolean_array[index_j] is True:
        # Set the current index in boolean_array to False
        boolean_array[index_j] = False
    
    # Increment increment_i by 1
    increment_i += 1
    
    # Update index_j to the next index using the formula
    index_j = (index_j + increment_i) % array_size

# Create a list x that contains all True values from boolean_array
true_values_list = [value for value in boolean_array if value]

# Check the length of the list true_values_list
if len(true_values_list) == 0:
    # If true_values_list is empty, output 'YES'
    print('YES')
else:
    # If true_values_list is not empty, output 'NO'
    print('NO')
