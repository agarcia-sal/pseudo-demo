# Get input from user and store its absolute value
target_number = abs(int(input()))

# Initialize counter to track the current integer
counter = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first 'counter' integers
    current_sum = (counter * (counter + 1)) // 2

    # Calculate the difference between current_sum and target_number
    difference = current_sum - target_number

    # Check if current_sum equals target_number
    if current_sum == target_number:
        print(counter)  # Print the counter and exit
        break

    # Check if current_sum exceeds target_number
    if current_sum > target_number:
        if difference % 2 == 0:  # Check if difference is even
            print(counter)  # Print the counter and exit
            break

    # Increment the counter for the next iteration
    counter += 1
