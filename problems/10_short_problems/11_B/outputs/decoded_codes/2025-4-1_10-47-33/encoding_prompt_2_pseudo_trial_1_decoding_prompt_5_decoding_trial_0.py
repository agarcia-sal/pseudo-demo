# Function to find the currentIndex based on the sum of natural numbers and a target number
def find_index():
    # Read an integer value from the user and take its absolute value
    target_number = abs(int(input()))
    
    # Initialize currentIndex
    current_index = 0
    
    # Enter an infinite loop
    while True:
        # Calculate the sum of the first currentIndex natural numbers
        current_sum = current_index * (current_index + 1) // 2  # Sum of first n natural numbers
        
        # Calculate the difference between currentSum and targetNumber
        difference = current_sum - target_number
        
        # Check if currentSum equals targetNumber
        if current_sum == target_number:
            print(current_index)  # Display currentIndex as the result
            break
        # Check if currentSum is greater than targetNumber
        elif current_sum > target_number:
            # Check if difference is an even number
            if difference % 2 == 0:
                print(current_index)  # Display currentIndex as the result
                break
        
        # Increment currentIndex by 1
        current_index += 1

# Call the function to execute
find_index()
