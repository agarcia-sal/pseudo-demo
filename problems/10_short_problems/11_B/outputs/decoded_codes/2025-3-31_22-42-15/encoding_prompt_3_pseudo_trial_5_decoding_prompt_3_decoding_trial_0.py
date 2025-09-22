# Function to find the index of the first natural number whose sum matches or exceeds a target sum
def find_target_index():
    # Read an absolute integer input from the user
    target_sum = abs(int(input()))
    
    # Initialize index to track the current sequence number
    index = 0

    # Continuous loop until a break condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between current_sum and target_sum
        difference = current_sum - target_sum
        
        # Check if current_sum exactly equals target_sum
        if current_sum == target_sum:
            print(index)  # Output the current index
            break  # Exit the loop
        
        # Check if current_sum exceeds target_sum
        elif current_sum > target_sum:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop

        # Increment index to check the next number in the next iteration
        index += 1

# Running the function
find_target_index()
