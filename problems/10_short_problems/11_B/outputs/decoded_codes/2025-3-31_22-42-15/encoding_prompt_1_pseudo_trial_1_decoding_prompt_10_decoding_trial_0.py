def find_index_for_target_sum():
    # Get the absolute value of the target sum from the user
    target_sum = abs(int(input()))
    
    index = 0  # Initialize index

    while True:  # Repeat indefinitely
        # Calculate the current sum of the first `index` natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between current_sum and target_sum
        difference = current_sum - target_sum
        
        # Check if current_sum equals target_sum
        if current_sum == target_sum:
            print(index)  # Print the current value of index
            break  # Exit the loop
        
        # Check if current_sum is greater than target_sum
        if current_sum > target_sum:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)  # Print the current value of index
                break  # Exit the loop
        
        index += 1  # Increment index

# Invoke the function to execute the logic
find_index_for_target_sum()
