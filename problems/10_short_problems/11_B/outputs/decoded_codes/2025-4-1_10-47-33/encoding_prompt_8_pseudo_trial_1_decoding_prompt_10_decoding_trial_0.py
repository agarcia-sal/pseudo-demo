def find_smallest_integer():
    # Get input from the user
    target_number = int(input())
    
    # Initialize the variable to track the current integer
    current_integer = 0
    
    # Loop to find the smallest non-negative integer
    while True:
        # Calculate the sum of integers from 0 to current_integer
        sum_of_integers = sum(range(current_integer + 1))
        
        # Calculate the difference between the sum and the target number
        difference = sum_of_integers - target_number
        
        # Check if the sum equals the target number
        if sum_of_integers == target_number:
            print(current_integer)  # Print the solution
            break
            
        # Check if the sum is greater than the target number
        elif sum_of_integers > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_integer)  # Print the solution
                break
        
        # Increment current_integer to consider the next integer
        current_integer += 1

# Call the function to execute the logic
find_smallest_integer()
