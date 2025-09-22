# Start the program

# Receive an integer input from the user and take its absolute value
target_number = abs(int(input()))
# Initialize a counter variable
current_index = 0

# Enter an infinite loop
while True:
    # Calculate the sum of all integers from 0 to currentIndex
    sum_value = (current_index * (current_index + 1)) // 2
    # Determine the difference between sum_value and target_number
    difference_from_target = sum_value - target_number
    
    # Check if sum_value is equal to target_number
    if sum_value == target_number:
        print(current_index)
        break  # Exit the loop
    
    # If sum_value is greater than target_number
    if sum_value > target_number:
        # Check if the difference is even
        if difference_from_target % 2 == 0:
            print(current_index)
            break  # Exit the loop
    
    # Increment currentIndex by 1
    current_index += 1

# End of the program
