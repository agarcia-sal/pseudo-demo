# Function to determine the minimum number of consecutive integers starting from 0
# to match a target sum either directly or by removing an even difference
def find_minimum_consecutive_integers():
    # Get the absolute value of the target sum from user input
    target_sum = abs(int(input()))
    
    # Initialize current index (current consecutive integer)
    index = 0
    
    # Infinite loop to find the minimum index
    while True:
        # Calculate the total sum of integers from 0 to index
        total_sum = (index * (index + 1)) // 2  # Sum formula for consecutive integers
        
        # Calculate the difference between total_sum and target_sum
        difference = total_sum - target_sum
        
        # Check if total_sum equals target_sum
        if total_sum == target_sum:
            print(index)
            break  # Exit the loop if condition is met
        
        # Check if total_sum is greater than target_sum
        elif total_sum > target_sum:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop if condition is met
        
        # Increment index to check the next consecutive integer
        index += 1

# Example call to the function (uncomment below to run)
# find_minimum_consecutive_integers()

# Note: To test the function, you can call it and input different values.
