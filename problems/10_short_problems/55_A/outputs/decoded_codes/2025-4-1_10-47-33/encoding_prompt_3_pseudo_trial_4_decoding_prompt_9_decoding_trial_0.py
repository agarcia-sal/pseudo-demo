# Read an integer value for the total count
total_count = int(input())

# Initialize a list with 'total_count' elements, all initially set to True
status_list = [True] * total_count

# Initialize two counters
outer_counter = 1
index_counter = 0

# Loop while the outer counter is less than or equal to 500,000
while outer_counter <= 500000:
    # If the current position in status_list is True
    if status_list[index_counter] == True:
        # Set the current position to False
        status_list[index_counter] = False
    
    # Increment the outer counter
    outer_counter += 1
    
    # Update the index_counter using modulo operation to wrap around
    index_counter = (index_counter + outer_counter) % total_count

# Filter the status_list to find all elements that are still True
remaining_true = [status for status in status_list if status]

# Check if there are no True elements remaining
if len(remaining_true) == 0:
    print('YES')
else:
    print('NO')
