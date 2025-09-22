# Get the absolute value of the input number
target_number = abs(int(input()))

# Initialize a counter to track the current integer
counter = 0

# Start an infinite loop to find the required integer
while True:
    # Calculate the sum of the first 'counter' integers
    current_sum = (counter * (counter + 1)) // 2

    # Calculate the difference between current sum and target number
    difference = current_sum - target_number

    # Check if the current sum equals the target number
    if current_sum == target_number:
        print(counter)
        break

    # Check if the current sum exceeds the target number
    if current_sum > target_number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(counter)
            break

    # Increment the counter for the next iteration
    counter += 1
