def find_integer():
    # Read input and convert to absolute integer
    target_value = abs(int(input()))
    
    # Initialize a counter
    counter = 0
    
    # Start an infinite loop
    while True:
        # Calculate the sum of the first `counter` natural numbers
        sum_of_natural_numbers = (counter * (counter + 1)) // 2
        
        # Determine the difference between the sum and the target value
        difference = sum_of_natural_numbers - target_value
        
        # Check if the sum equals the target value
        if sum_of_natural_numbers == target_value:
            print(counter)
            break
        
        # Check if the sum is greater than the target value
        elif sum_of_natural_numbers > target_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)
                break
            
        # Increment the counter for the next iteration
        counter += 1

# Call the function
find_integer()
