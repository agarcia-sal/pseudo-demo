# Function to calculate the maximum integer for a given condition based on user input
def calculate_max_integer():
    # Input handling: Read a number from the user and store its absolute value
    absolute_input = abs(int(input()))
    
    # Initialize a counter to keep track of the current integer
    index = 0
    
    # Infinite loop for calculation
    while True:
        # Calculate the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between current sum and absolute input
        difference = current_sum - absolute_input
        
        # Check conditions
        if current_sum == absolute_input:
            # Output the value of index as the result
            print(index)
            break
        elif current_sum > absolute_input:
            # If difference is an even number, output the value of index as the result
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the counter to consider the next integer
        index += 1

# Call the function to execute
calculate_max_integer()
