def find_index():
    # Read the absolute value of the integer input
    target_number = abs(int(input()))
    
    # Initialize an index variable
    index = 0

    # Continuously evaluate until a suitable condition is met
    while True:
        # Calculate the sum of the first 'index' integers
        current_sum = index * (index + 1) // 2
        
        # Calculate the difference between the current sum and the target number
        difference = current_sum - target_number
        
        # Check if the current sum equals the target number
        if current_sum == target_number:
            print(index)
            break
        
        # Check if the current sum exceeds the target number
        elif current_sum > target_number:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# Run the function to test its functionality
find_index()
