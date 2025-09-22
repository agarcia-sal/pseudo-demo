# Start of the program

# Read an integer input which defines the size of an array
array_size = int(input())  # Assign the input value to array_size

# Initialize a list of boolean values indicating active status, all set to True, of size array_size
boolean_list = [True] * array_size

# Initialize counters
index_counter = 0
step_increment = 1

# Loop until step_increment exceeds 500000
while step_increment <= 500000:

    # If the current position in the boolean list is True
    if boolean_list[index_counter] is True:
        
        # Mark this position as False, indicating it's been processed
        boolean_list[index_counter] = False

    # Increment step_increment after processing
    step_increment += 1
    
    # Update the index_counter using modulo to stay within bounds of boolean list length
    index_counter = (index_counter + step_increment) % array_size

# Create a new list containing only True values remaining in the boolean list
active_items = [item for item in boolean_list if item]

# Check if there are no True values remaining
if len(active_items) == 0:
    print("YES")
else:
    print("NO")

# End of the program
