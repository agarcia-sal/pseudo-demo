def find_smallest_integer():
    # Receive Input
    target_sum = int(input())
    
    # Initialize Variables
    current_index = 0
    
    # Infinite Loop
    while True:
        # Calculate the Sum
        current_sum = (current_index * (current_index + 1)) // 2
        
        # Calculate the Difference
        surplus = current_sum - target_sum
        
        # Check for Exact Match
        if current_sum == target_sum:
            print(current_index)
            break
        
        # Check for Surplus Condition
        if surplus > 0 and surplus % 2 == 0:
            print(current_index)
            break
        
        # Increment Index
        current_index += 1
        
# Call the function to execute the logic
find_smallest_integer()
