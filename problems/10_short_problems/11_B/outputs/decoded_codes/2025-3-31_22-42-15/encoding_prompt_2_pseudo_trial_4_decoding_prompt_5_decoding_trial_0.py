# Start of the program

# Read an integer value from the user and take its absolute value
target_number = abs(int(input()))

# Initialize the index variable to 0
index = 0

# Begin an infinite loop
while True:
    # Calculate the current sum as the sum of the first 'index' natural numbers
    current_sum = (index * (index + 1)) // 2
    
    # Calculate the difference between current sum and target number
    difference = current_sum - target_number
    
    # Check conditions
    if current_sum == target_number:
        print(index)  # Print the index if current sum equals target number
        break  # Exit the loop
    elif current_sum > target_number:
        # Check if difference is an even number
        if difference % 2 == 0:
            print(index)  # Print the index if difference is even
            break  # Exit the loop
    
    # Increment the index by 1
    index += 1

# End of the program
