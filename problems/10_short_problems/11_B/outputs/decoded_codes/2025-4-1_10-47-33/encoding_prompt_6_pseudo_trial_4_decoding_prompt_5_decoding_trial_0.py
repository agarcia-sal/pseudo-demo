# Function to find the smallest integer counter such that the sum of the first 'counter' integers 
# either equals or exceeds the absolute value of the given input
def find_integer_counter():
    # Read an integer input and take its absolute value
    absolute_value = abs(int(input()))
    
    # Initialize a counter variable
    counter = 0
    
    # Loop indefinitely until specific conditions are met
    while True:
        # Calculate the sum of the first 'counter' integers
        current_sum = (counter * (counter + 1)) // 2
        
        # Calculate the difference between current_sum and absolute_value
        difference = current_sum - absolute_value
        
        # Check if the current_sum equals the absolute_value
        if current_sum == absolute_value:
            print(counter)  # Output the counter value
            break  # Exit the loop
        
        # Check if current_sum exceeds absolute_value
        elif current_sum > absolute_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Output the counter value
                break  # Exit the loop
        
        # Increment the counter for the next iteration
        counter += 1

# Call the function to execute the program
find_integer_counter()
