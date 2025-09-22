def find_smallest_integer():
    # Get input and store its absolute value as targetSum
    target_sum = abs(int(input()))
    
    # Initialize a counter
    current_index = 0
    
    # Loop for calculation
    while True:
        # Calculate the sum of the first current_index integers
        current_sum = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between currentSum and targetSum
        difference = current_sum - target_sum
        
        # Check conditions
        if current_sum == target_sum:
            print(current_index)
            break
        elif current_sum > target_sum:
            if difference % 2 == 0:
                print(current_index)
                break
        
        # Increment currentIndex by 1
        current_index += 1

# Call the function to execute the algorithm
find_smallest_integer()
