# Function to find the smallest non-negative integer based on defined conditions
def find_smallest_integer():
    # Get user input and convert it to absolute value
    target_number = abs(int(input()))
    
    # Initialize the current index
    current_index = 0
    
    # Repeat indefinitely until conditions are met
    while True:
        # Calculate the sum of integers from 0 to current_index
        current_sum = sum(range(current_index + 1))
        
        # Calculate the difference between current_sum and target_number
        difference = current_sum - target_number
        
        # Check if current_sum equals target_number
        if current_sum == target_number:
            print(current_index)  # Print the answer
            break  # End the program
        
        # Check if current_sum exceeds target_number
        if current_sum > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)  # Print the answer
                break  # End the program
        
        # Increment current_index for the next iteration
        current_index += 1

# Call the function to execute the logic
find_smallest_integer()
