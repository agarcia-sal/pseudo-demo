# Start the Program
# Capture user input and convert it to a non-negative integer
input_value = abs(int(input()))

# Initialize a Counter
current_index = 0

# Create an Infinite Loop for Calculation
while True:
    # Calculate the Triangular Number
    triangular_sum = (current_index * (current_index + 1)) // 2

    # Determine the Difference
    difference = triangular_sum - input_value

    # Check for Exact Match
    if triangular_sum == input_value:
        print(current_index)  # Output the value of currentIndex
        break  # Exit the loop

    # Check for Condition When Triangular Sum Exceeds Input Value
    if triangular_sum > input_value:
        if difference % 2 == 0:  # If difference is even
            print(current_index)  # Output the value of currentIndex
            break  # Exit the loop

    # Increment the Counter
    current_index += 1

# End the Program
