# Function to find the largest integer representing the number of sequentially summed integers
def find_largest_sum_index():
    # Step 1: Get the absolute value of input number
    target_value = abs(int(input()))
    
    # Step 2: Initialize counter
    counter = 0
    
    # Step 3: Infinite loop to find the solution
    while True:
        # Step 4: Calculate the sum of the first 'counter' integers
        current_sum = counter * (counter + 1) // 2
        
        # Step 5: Calculate the difference from the target value
        difference = current_sum - target_value
        
        # Step 6: Check if current_sum equals target_value
        if current_sum == target_value:
            return counter
        
        # Step 7: Check if current_sum exceeds target_value
        if current_sum > target_value:
            # Check if difference is even
            if difference % 2 == 0:
                return counter
        
        # Step 8: Increment counter
        counter += 1

# Example usage:
# result = find_largest_sum_index()
# print(result)

