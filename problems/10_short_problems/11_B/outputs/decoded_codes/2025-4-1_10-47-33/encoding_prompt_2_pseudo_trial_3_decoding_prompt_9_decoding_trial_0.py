# Start the program
target_number = abs(int(input()))  # Receive integer input and take absolute value
current_index = 0  # Initialize the counter variable

while True:  # Enter an infinite loop
    sum_value = (current_index * (current_index + 1)) // 2  # Calculate sum from 0 to currentIndex using the formula
    difference_from_target = sum_value - target_number  # Determine the difference from targetNumber
    
    # Check if sumValue is equal to targetNumber
    if sum_value == target_number:
        print(current_index)  # Print currentIndex
        break  # Exit the loop
        
    # If sumValue is greater than targetNumber
    if sum_value > target_number:
        # Check if differenceFromTarget is even
        if difference_from_target % 2 == 0:
            print(current_index)  # Print currentIndex
            break  # Exit the loop
            
    current_index += 1  # Increment currentIndex by 1
# End the program
