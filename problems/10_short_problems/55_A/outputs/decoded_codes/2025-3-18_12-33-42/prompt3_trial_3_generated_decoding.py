# Accept an integer input representing the size of the list
size_of_list = int(input())

# Create a list to track flags, initialized to True for all elements
flags_list = [True] * size_of_list

# Initialize two tracking variables
step_counter = 1
index_counter = 0

# Loop through numbers from 1 to 500,000
while step_counter <= 500000:
    # If the current index in flags_list is True
    if flags_list[index_counter]:
        # Set the current index to False
        flags_list[index_counter] = False

    # Move to the next step
    step_counter += 1
    
    # Update the index_counter, wrapping around if it exceeds size_of_list
    index_counter = (index_counter + step_counter) % size_of_list

# Create a new list of values from flags_list that are still True
remaining_true_flags = [flag for flag in flags_list if flag]

# Check if there are any True values left in remaining_true_flags
if len(remaining_true_flags) == 0:
    # If no True values are found, print 'YES'
    print('YES')
else:
    # Otherwise, print 'NO'
    print('NO')
