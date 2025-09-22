# Read an integer input representing the size of the array
size_of_array = int(input())

# Create a boolean array initialized to True
boolean_array = [True] * size_of_array

# Initialize index j to 0
index_j = 0
# Initialize counter i to 1
counter_i = 1

# Loop while counter i is less than or equal to 500000
while counter_i <= 500000:
    # Check if the current index in boolean_array is True
    if boolean_array[index_j]:
        # Set the current index to False
        boolean_array[index_j] = False
    
    # Increment counter i
    counter_i += 1
    
    # Update index j using circular indexing with the size of the array
    index_j = (index_j + counter_i) % size_of_array

# Create a list x containing all True values from boolean_array
true_values = [value for value in boolean_array if value]

# Check the length of the list true_values
if len(true_values) == 0:
    print('YES')  # Output YES if no True values remain
else:
    print('NO')   # Output NO if some True values remain
