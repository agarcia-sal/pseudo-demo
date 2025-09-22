# Start of the program

# Accept an integer input for the size of a list
list_size = int(input())

# Create a list called status_list with list_size elements, all initially set to True
status_list = [True] * list_size

# Set up variables
index_position = 0
increment_value = 1

# Loop operations while increment_value is less than or equal to 500,000
while increment_value <= 500000:
    # Check if the element at index_position in status_list is True
    if status_list[index_position]:
        # Change it to False indicating it has been processed
        status_list[index_position] = False
    
    # Increase increment_value by 1
    increment_value += 1
    
    # Update index_position with wrap-around using modulo operation
    index_position = (index_position + increment_value) % list_size

# Create a new list remaining_true that includes all elements from status_list that are still True
remaining_true = [status for status in status_list if status]

# Output result
if len(remaining_true) == 0:
    print("YES")  # All values have been processed
else:
    print("NO")   # Some values are still True

# End of the program
