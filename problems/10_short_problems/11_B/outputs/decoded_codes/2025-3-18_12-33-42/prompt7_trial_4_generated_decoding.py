def find_special_integer():
    # Prompt user for an integer input
    user_input = int(input())
    
    # Set the absolute value of the input
    absolute_value = abs(user_input)
    
    # Initialize the index for computation
    index = 0
    
    # Infinite loop to find the special integer
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_of_first_index = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute value
        difference = sum_of_first_index - absolute_value
        
        # Check if the sum is exactly equal to the absolute value
        if sum_of_first_index == absolute_value:
            print(index)  # Found a match, print the index
            break  # Exit the loop
        
        # Check if the sum is greater than the absolute value
        elif sum_of_first_index > absolute_value:
            # If the difference is even, print the index
            if difference % 2 == 0:
                print(index)  # Condition satisfied, print the index
                break  # Exit the loop
        
        # Increment index for the next iteration
        index += 1

# This is the main check to run the function
if __name__ == "__main__":
    find_special_integer()
