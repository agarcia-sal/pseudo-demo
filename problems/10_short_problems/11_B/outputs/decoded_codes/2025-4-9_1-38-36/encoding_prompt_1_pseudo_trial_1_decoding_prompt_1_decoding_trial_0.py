# Define Main Function
def find_integer_matching_input():
    # Get Input
    target_value = abs(int(input()))
    
    # Initialize Variables
    index = 0
    
    # Start Infinite Loop
    while True:
        # Calculate sumToIndex
        sum_to_index = index * (index + 1) / 2
        
        # Calculate difference
        difference = sum_to_index - target_value
        
        # Check if Matches and Conditions
        if sum_to_index == target_value:
            print(index)
            break  # Exit the loop (function)
        elif sum_to_index > target_value:
            if difference % 2 == 0:  # Check if difference is even
                print(index)
                break  # Exit the loop (function)
        
        # Increment index by 1
        index += 1
