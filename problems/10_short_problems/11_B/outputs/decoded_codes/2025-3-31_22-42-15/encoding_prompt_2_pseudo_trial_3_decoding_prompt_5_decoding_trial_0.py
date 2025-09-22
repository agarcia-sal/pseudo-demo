# Function to find the smallest non-negative integer that meets specific conditions based on a given number
def find_smallest_integer():
    # Read an integer value and take its absolute value
    target_value = abs(int(input()))
    
    # Initialize index to 0
    index = 0
    
    # Loop until a condition is met
    while True:
        # Calculate the current sum using the formula for the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2
        
        # Compute the difference between current sum and target value
        difference = current_sum - target_value
        
        # Check if current sum is equal to target value
        if current_sum == target_value:
            print(index)
            break
        
        # If current sum is greater than target value
        if current_sum > target_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index for the next iteration
        index += 1

# Example test cases (These would normally be run when calling the function)
# Test with input 5:
# Input: 5 -> Output should be 5
# Test with input 10:
# Input: 10 -> Output should be 4
