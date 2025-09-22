# Function to determine if any True values remain in the boolean list after processing
def check_remaining_trues():
    # Read the integer input which represents the size of the list
    size_of_list = int(input())
    
    # Create a boolean list initialized to True with the specified size
    boolean_list = [True] * size_of_list
    
    # Initialize loop counters
    counter = 1
    current_index = 0
    
    # Loop until counter exceeds 500,000
    while counter <= 500000:
        # If the current index in the boolean list is True
        if boolean_list[current_index]:
            # Mark the current index as False
            boolean_list[current_index] = False
        
        # Increment the counter
        counter += 1
        
        # Update currentIndex based on the modulo of sizeOfList
        current_index = (current_index + counter) % size_of_list
    
    # Create a list of all True values from the boolean list
    remaining_true_values = [value for value in boolean_list if value]
    
    # Check if any True values remain
    if len(remaining_true_values) == 0:
        # If no True values left, print "YES"
        print("YES")
    else:
        # If there are True values left, print "NO"
        print("NO")

# Example usage
check_remaining_trues()
