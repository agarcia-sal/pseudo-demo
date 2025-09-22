# Function to find a non-negative integer corresponding to user input based on triangular numbers
def find_triangular_index():
    # Capture the user input and convert it to a non-negative integer
    input_value = abs(int(input()))  # Read input and take absolute value

    # Initialize a counter
    current_index = 0

    while True:  # Start an infinite loop for calculation
        # Calculate the triangular number using the formula: n(n + 1) / 2
        triangular_sum = (current_index * (current_index + 1)) // 2

        # Calculate the difference between the triangular sum and the input value
        difference = triangular_sum - input_value

        # Check for an exact match
        if triangular_sum == input_value:
            print(current_index)  # Output the index
            break  # Exit the loop

        # Check if the triangular sum exceeds input value
        if triangular_sum > input_value:
            # Check if the difference is even
            if difference % 2 == 0:
                print(current_index)  # Output the index
                break  # Exit the loop

        # Increment the counter for the next triangular number
        current_index += 1

# Call the function to execute the program
find_triangular_index()
