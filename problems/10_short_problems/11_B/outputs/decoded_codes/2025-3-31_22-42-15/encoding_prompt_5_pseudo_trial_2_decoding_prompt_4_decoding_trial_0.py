# Function to find the smallest non-negative integer based on the given conditions
def find_smallest_integer():
    # Get user input and convert it to absolute value
    target_number = abs(int(input()))
    
    # Initialize counter
    current_index = 0
    
    while True:  # Loop indefinitely
        # Calculate the sum of all integers from 0 to current_index
        current_sum = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between current_sum and target_number
        difference = current_sum - target_number
        
        # Check if the current_sum is equal to the target_number
        if current_sum == target_number:
            print(current_index)  # Print the answer
            return
        
        # If current_sum is greater than target_number, check the difference
        if current_sum > target_number:
            if difference % 2 == 0:  # Check if the difference is even
                print(current_index)  # Print the answer
                return
        
        # Increment the current_index for the next iteration
        current_index += 1

# Call the function to execute the program
find_smallest_integer()
