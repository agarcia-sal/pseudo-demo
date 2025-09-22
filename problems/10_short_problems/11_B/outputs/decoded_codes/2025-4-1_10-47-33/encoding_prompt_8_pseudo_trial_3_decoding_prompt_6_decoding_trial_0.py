# Initialize the target number as the absolute value of the input
target_number = abs(int(input()))

# Initialize the index variable
index = 0

# Start an infinite loop
while True:
    # Calculate the sum of integers from 0 to index using the formula
    sum_to_index = (index * (index + 1)) // 2  # Use integer division

    # Calculate the difference between the sum and target_number
    difference = sum_to_index - target_number

    # Check for an exact match
    if sum_to_index == target_number:
        print(index)
        break  # Exit the loop if there's an exact match

    # Check if the sum has exceeded the target_number
    if sum_to_index > target_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop if the difference is even

    # Increment index for the next iteration
    index += 1
