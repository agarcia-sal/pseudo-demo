# Function to find a non-negative integer such that 
# the sum of the first 'i' integers equals 'n' or 
# the difference is an even number.
def find_integer():
    # Input the target sum from the user
    target_sum = abs(int(input()))
    
    # Initialize the counter variable
    index = 0
    
    # Begin infinite loop to find the valid index
    while True:
        # Calculate the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between current sum and target sum
        difference = current_sum - target_sum
        
        # Check for equality
        if current_sum == target_sum:
            print(index)  # Output the index
            break
        
        # Check if the current sum exceeds the target sum
        if current_sum > target_sum:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break
        
        # Increment the counter
        index += 1

# Execute the function to perform the task
find_integer()
