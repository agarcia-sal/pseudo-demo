# Define the main function to execute the logic
def main():
    # Step 1: Read integer input representing the size of the list
    list_size = int(input())
    
    # Step 2: Initialize a list of boolean values, all set to True
    is_active = [True] * list_size
    
    # Step 3: Initialize control variables
    index_increment = 1
    current_index = 0
    
    # Step 4: Iterate through a range up to 500000
    while current_index <= 500000:
        # Step 5: Check the boolean value at the current index
        if is_active[current_index]:
            # Mark the current index as inactive
            is_active[current_index] = False
        
        # Step 6: Update the index values
        index_increment += 1
        current_index = (current_index + index_increment) % list_size
    
    # Step 7: Extract all True values from the is_active list
    active_elements = [index for index, value in enumerate(is_active) if value]
    
    # Step 8: Check if the active_elements list is empty
    if len(active_elements) == 0:
        # If there are no active elements, print YES
        print('YES')
    else:
        # If there are active elements, print NO
        print('NO')

# Execute the main function
main()
