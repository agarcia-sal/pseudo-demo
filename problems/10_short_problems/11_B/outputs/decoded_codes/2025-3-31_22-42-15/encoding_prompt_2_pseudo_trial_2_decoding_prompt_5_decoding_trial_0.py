# Function to find the index of natural numbers whose sum matches or has an even difference with targetSum
def find_index_matching_sum():
    # Read an integer value and take its absolute value
    target_sum = abs(int(input()))
    
    # Initialize the counter index
    index = 0
    
    # Start an infinite loop
    while True:
        # Calculate the sum of the first index natural numbers
        current_sum = index * (index + 1) // 2
        
        # Calculate the difference between currentSum and targetSum
        difference = current_sum - target_sum
        
        # Check for exact match
        if current_sum == target_sum:
            print(index)
            break
        
        # Check if currentSum overshoots targetSum
        if current_sum > target_sum:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment index
        index += 1

# Example of how to run the function
find_index_matching_sum()
