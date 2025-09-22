def find_target_index():
    # Read an integer value from the user and take its absolute value
    target_number = abs(int(input()))
    
    # Initialize current_index to 0
    current_index = 0
    
    while True:
        # Calculate the sum of the first current_index natural numbers
        current_sum = current_index * (current_index + 1) // 2
        
        # Determine the difference between current_sum and target_number
        difference = current_sum - target_number
        
        # Check if current_sum matches target_number
        if current_sum == target_number:
            print(current_index)
            break
        
        # Check if current_sum exceeds target_number
        elif current_sum > target_number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(current_index)
                break
        
        # Increment current_index by 1
        current_index += 1

# Call the function to execute the code
find_target_index()
