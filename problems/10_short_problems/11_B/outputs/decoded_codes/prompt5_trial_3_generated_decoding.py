# Get the absolute value of user input and store it in targetNumber
target_number = abs(int(input()))

# Initialize currentIndex to 0
current_index = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first currentIndex natural numbers
    current_sum = (current_index * (current_index + 1)) // 2
    
    # Calculate the difference as currentSum minus targetNumber
    remainder = current_sum - target_number

    # Check if currentSum is equal to targetNumber
    if current_sum == target_number:
        print(current_index)  # This is the answer
        break

    # Check if currentSum is greater than targetNumber
    if current_sum > target_number:
        # Check if remainder is an even number
        if remainder % 2 == 0:
            print(current_index)  # This is a valid solution
            break

    # Increment currentIndex by 1 to explore the next number
    current_index += 1
