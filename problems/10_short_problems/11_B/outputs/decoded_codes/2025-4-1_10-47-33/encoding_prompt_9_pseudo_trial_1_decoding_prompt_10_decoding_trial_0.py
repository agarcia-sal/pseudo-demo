def find_smallest_integer(target_sum):
    current_index = 0  # Initialize the current integer to evaluate

    while True:  # Loop indefinitely until a valid integer is found
        # Calculate the sum of integers from 0 to current_index
        current_sum = current_index * (current_index + 1) // 2  # Using integer division

        # Calculate the difference between current sum and target sum
        difference = current_sum - target_sum

        # Check if the current sum equals the target sum
        if current_sum == target_sum:
            return current_index  # Found a match

        # Check if the current sum exceeds the target sum
        if current_sum > target_sum:
            if difference % 2 == 0:  # Check if the difference is even
                return current_index  # Found an overshoot that can be adjusted

        # Increment the index to evaluate the next integer
        current_index += 1

if __name__ == "__main__":
    # Get input from the user
    user_input = int(input())  # Convert input directly to an integer
    target_sum = abs(user_input)  # Calculate the absolute value

    result = find_smallest_integer(target_sum)  # Call the function
    print(result)  # Output the result
