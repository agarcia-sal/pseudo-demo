# Function to find the smallest non-negative integer whose sum 
# of the first i natural numbers meets the specified conditions
def find_smallest_integer():
    # Get the absolute value of the integer input from the user
    absolute_value = abs(int(input()))
    
    # Initialize the current index to 0
    current_index = 0
    
    # Start an indefinite loop to find the required integer
    while True:
        # Calculate the sum of the first current_index natural numbers
        sum_of_numbers = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between sum_of_numbers and absolute_value
        difference = sum_of_numbers - absolute_value
        
        # Check if the sum is exactly equal to the absolute value
        if sum_of_numbers == absolute_value:
            print(current_index)
            break
        # Check if the sum exceeds the absolute value
        elif sum_of_numbers > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)
                break
            
        # Increment current_index for the next iteration
        current_index += 1

# Call the function to execute
find_smallest_integer()
