def find_smallest_integer():
    # Get input from the user and store its absolute value
    target_number = abs(int(input()))
    
    # Initialize counter to keep track of current integer
    counter = 0
    
    while True:
        # Calculate the sum of the first 'counter' integers
        current_sum = (counter * (counter + 1)) // 2
        
        # Calculate the difference between current sum and target number
        difference = current_sum - target_number
        
        # Check if current sum equals target number
        if current_sum == target_number:
            print(counter)
            break
        
        # Check if current sum exceeds target number
        if current_sum > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)
                break
        
        # Increment the counter for the next iteration
        counter += 1

# Call the function to execute the process
find_smallest_integer()
