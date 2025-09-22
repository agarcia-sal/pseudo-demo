# This function finds the smallest non-negative integer such that
# the sum of the first i integers equals or can be adjusted to equal a given targetSum.

def find_smallest_integer():
    # Get input from the user and ensure it's a non-negative integer
    target_sum = abs(int(input()))

    # Initialize the counter for the loop
    current_index = 0

    # Loop indefinitely to find the desired integer
    while True:
        # Calculate the sum of the first current_index integers
        current_sum = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between current_sum and target_sum
        difference = current_sum - target_sum
        
        # Check if current_sum equals target_sum
        if current_sum == target_sum:
            print(current_index)
            break
        
        # Check if current_sum is greater than target_sum
        if current_sum > target_sum:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)
                break
        
        # Increment current_index for the next iteration
        current_index += 1

# Call the function to execute
find_smallest_integer()
