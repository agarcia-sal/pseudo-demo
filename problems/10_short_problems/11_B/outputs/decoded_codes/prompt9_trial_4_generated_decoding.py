# Get user input and store the absolute value
target_value = abs(int(input()))

# Initialize the counter
index = 0

# Begin infinite loop
while True:
    # Calculate the triangular number
    triangular_number = index * (index + 1) // 2

    # Calculate the difference
    difference = triangular_number - target_value

    # Check if the triangular number is equal to the target value
    if triangular_number == target_value:
        print(index)
        break  # Exit the loop

    # Check if the triangular number is greater than the target value
    elif triangular_number > target_value:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)
            break  # Exit the loop

    # Increment the counter
    index += 1
