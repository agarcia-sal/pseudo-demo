# Start Program

# Get Input
total_count = int(input())  # Read the integer value for the size of the list

# Initialize List
status_list = [True] * total_count  # Create a list of 'total_count' elements, all set to True

# Set Starting Values
current_index = 0  # This keeps track of which element is being processed
counter = 1  # This determines how far to jump in the list

# Process the List
while counter <= 500000:
    if status_list[current_index]:  # Check if the current element is True
        status_list[current_index] = False  # Mark the current element as False
    counter += 1  # Increment the counter by 1
    current_index = (current_index + counter) % total_count  # Update the current index

# Check Results
unmarked_elements = [element for element in status_list if element]  # Get all unmarked (True) elements

# Output Result
if len(unmarked_elements) == 0:  # If there are no unmarked elements
    print("YES")  # All elements were marked
else:
    print("NO")  # Some elements remain unmarked

# End Program
