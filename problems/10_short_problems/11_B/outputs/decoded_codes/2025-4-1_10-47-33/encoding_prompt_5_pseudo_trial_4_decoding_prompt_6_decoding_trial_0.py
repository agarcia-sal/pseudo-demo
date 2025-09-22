def find_smallest_integer():
    # Get absolute value of an input number
    number = abs(int(input()))  # Convert input to integer and take absolute value

    # Initialize a counter variable
    index = 0

    # Continuously search for a valid integer
    while True:
        # Calculate the current triangular number
        triangular_number = (index * (index + 1)) // 2

        # Calculate the difference between the triangular number and the input number
        difference = triangular_number - number

        # Check if the triangular number equals the input number
        if triangular_number == number:
            print(index)  # Output the index
            break

        # Check if the triangular number is greater than the input number
        elif triangular_number > number:
            # Verify if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break

        # Increment the index for the next triangular number
        index += 1

# Call the function to execute
find_smallest_integer()
