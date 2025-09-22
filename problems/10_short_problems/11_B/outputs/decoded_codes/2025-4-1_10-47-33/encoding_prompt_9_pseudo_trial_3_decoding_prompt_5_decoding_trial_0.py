# Function to find the smallest non-negative integer whose sum of integers up to that point
# equals or exceeds a target value by an even amount.
def find_smallest_integer():
    # Receive input for target value and convert to absolute integer
    target_value = abs(int(input()))  # Get user input
    
    # Initialize index as a counter
    index = 0

    # Infinite loop to calculate sums and check conditions
    while True:
        # Calculate the current sum of integers from 0 to index
        current_sum = (index * (index + 1)) // 2  # Use integer division to ensure result is integer
        
        # Calculate the difference between current sum and target value
        diff = current_sum - target_value
        
        # Check if current sum equals the target value
        if current_sum == target_value:
            print(index)  # Output the current index
            break  # Exit loop if condition is met
        
        # Check if current sum is greater than the target value
        if current_sum > target_value:
            # Check if the difference is even
            if diff % 2 == 0:
                print(index)  # Output the current index
                break  # Exit loop if condition is met
        
        # Increment index for the next iteration
        index += 1

# Test cases can be executed by calling the function
# Example input: 5 would expect an output of 3 since 0+1+2=3 < 5, and 0+1+2+3=6 > 5 and is even.
