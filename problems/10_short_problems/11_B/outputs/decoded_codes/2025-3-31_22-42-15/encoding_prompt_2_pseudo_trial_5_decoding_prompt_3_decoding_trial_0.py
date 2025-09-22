# Function to find the required currentIndex based on the target sum
def find_index_for_target_sum():
    # Input the integer value from the user and store its absolute value
    target_sum = abs(int(input()))
    
    # Initialize the current index counter
    current_index = 0
    
    # Start an infinite loop that will only terminate upon meeting conditions
    while True:
        # Calculate the sum of the first current_index integers
        sum_of_series = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference between the sum and the target sum
        difference = sum_of_series - target_sum
        
        # Check if the sum of the series equals the target sum
        if sum_of_series == target_sum:
            print(current_index)
            break
        
        # If the sum is greater than the target sum, check if the difference is even
        if sum_of_series > target_sum and difference % 2 == 0:
            print(current_index)
            break
        
        # Increment the current index and continue the loop
        current_index += 1

# Call the function to execute
find_index_for_target_sum()
