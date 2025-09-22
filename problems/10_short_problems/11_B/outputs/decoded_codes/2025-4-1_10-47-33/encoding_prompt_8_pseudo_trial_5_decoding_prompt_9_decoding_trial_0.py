# Start the Program
input_value = abs(int(input()))  # Capture user input and store as a non-negative integer

# Initialize a Counter
current_index = 0

# Create an Infinite Loop for Calculation
while True:
    # Calculate the Triangular Number
    triangular_sum = (current_index * (current_index + 1)) // 2  # Triangular number calculation

    # Determine the Difference
    difference = triangular_sum - input_value  # Calculate the difference

    # Check for Exact Match
    if triangular_sum == input_value:
        print(current_index)  # Output the value of currentIndex
        break  # Exit the loop

    # Check for Condition When Triangular Sum Exceeds Input Value
    if triangular_sum > input_value:
        if difference % 2 == 0:  # Check if the difference is even
            print(current_index)  # Output the value of currentIndex as valid result
            break  # Exit the loop

    # Increment the Counter
    current_index += 1  # Increase the value of currentIndex by 1

# End the Program
