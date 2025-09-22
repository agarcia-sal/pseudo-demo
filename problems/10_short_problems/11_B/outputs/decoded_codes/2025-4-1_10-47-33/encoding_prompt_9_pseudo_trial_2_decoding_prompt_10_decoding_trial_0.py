def find_smallest_integer():
    # Get the input from the user and convert it to a non-negative integer
    target_number = abs(int(input()))
    
    # Initialize the current integer to zero
    current_integer = 0
    
    while True:
        # Calculate the sum of the first 'current_integer' integers
        sum_of_integers = (current_integer * (current_integer + 1)) // 2
        
        # Calculate the difference between the sum of integers and the target number
        difference = sum_of_integers - target_number
        
        # Check if the sum equals the target number
        if sum_of_integers == target_number:
            print(current_integer)
            break
        
        # Check if the sum exceeds the target number
        if sum_of_integers > target_number:
            # If the difference is even, print the current integer and exit
            if difference % 2 == 0:
                print(current_integer)
                break
        
        # Increment the current integer to check the next value
        current_integer += 1

# Call the function to execute
find_smallest_integer()
