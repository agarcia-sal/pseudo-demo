# Function to find the smallest non-negative integer whose sum of consecutive integers
# either equals or exceeds a given absolute input number
def find_smallest_integer():
    # Get input from user and calculate the absolute value
    target_sum = abs(int(input()))
    
    # Initialize the current counter
    current_index = 0
    
    # Loop indefinitely to evaluate consecutive integers
    while True:
        # Calculate the sum of all integers from 0 to current_index
        current_sum = current_index * (current_index + 1) // 2
        
        # Calculate the difference between current_sum and target_sum
        difference = current_sum - target_sum
        
        # Check for exact match
        if current_sum == target_sum:
            print(current_index)  # Output the result
            break  # Terminate the loop
        
        # Check for overshoot
        if current_sum > target_sum:
            if difference % 2 == 0:  # Check if the difference is even
                print(current_index)  # Output the result
                break  # Terminate the loop
        
        # Increment the current index to evaluate the next integer
        current_index += 1

# Run the function to find the smallest integer
find_smallest_integer()
