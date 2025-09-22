# BEGIN

# Input the size of the list
size_of_list = int(input())

# Initialize a list of boolean values all set to True
boolean_list = [True] * size_of_list

# Initialize index variables
index_increment = 1
current_index = 0

# Loop to mark elements in booleanList
while index_increment <= 500000:
    # Check if the current index in booleanList is True
    if boolean_list[current_index] is True:
        # Mark the current index as False
        boolean_list[current_index] = False

    # Increment the index for the next step
    index_increment += 1
    
    # Update the currentIndex based on the next increment
    current_index = (current_index + index_increment) % size_of_list

# Create a list of all True values from booleanList
filtered_true_values = [value for value in boolean_list if value is True]

# Check if filteredTrueValues is empty
if len(filtered_true_values) == 0:
    print('YES')
else:
    print('NO')

# END
