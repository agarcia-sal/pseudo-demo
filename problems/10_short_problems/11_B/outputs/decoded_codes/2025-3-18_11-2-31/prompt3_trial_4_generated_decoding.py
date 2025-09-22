def find_index_with_sum():
    # Read input value and store it as an absolute integer
    input_number = abs(int(input()))

    # Initialize a variable to keep track of the current step or index
    current_index = 0

    # Loop indefinitely until a break condition is met
    while True:
        # Calculate the sum of the first 'currentIndex' integers
        sum_numbers = (current_index * (current_index + 1)) // 2  # // for integer division

        # Calculate the difference between the sum and input number
        difference = sum_numbers - input_number

        # If the calculated sum equals the input number
        if sum_numbers == input_number:
            # Output the current index as the result
            print(current_index)
            break

        # If the calculated sum is greater than the input number
        elif sum_numbers > input_number:
            # Check if the difference is even
            if difference % 2 == 0:
                # Output the current index as the result
                print(current_index)
                break

        # Increment the current index for the next iteration
        current_index += 1
