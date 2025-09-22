# Function to process a list of boolean values based on a given input size
def process_boolean_array():
    # Read the integer input which defines the size of the array
    array_size = int(input())
    
    # Initialize a list of boolean values indicating active status
    boolean_list = [True] * array_size
    
    # Initialize counters
    index_counter = 0
    step_increment = 1
    
    # Loop until step_increment exceeds 500000
    while step_increment <= 500000:
        # If the current position in the boolean list is True
        if boolean_list[index_counter]:
            # Mark this position as False, indicating it's been processed
            boolean_list[index_counter] = False
        
        # Increment step_increment after processing
        step_increment += 1
        
        # Update the index_counter using modulo to stay within bounds of boolean list length
        index_counter = (index_counter + step_increment) % array_size
    
    # Create a new list containing only True values remaining in the boolean list
    active_items = [value for value in boolean_list if value]
    
    # Check if there are no True values remaining
    if len(active_items) == 0:
        print("YES")
    else:
        print("NO")

# Call the function to execute
process_boolean_array()
