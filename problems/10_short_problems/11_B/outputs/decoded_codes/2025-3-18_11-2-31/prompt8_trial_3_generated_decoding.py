def find_count():
    # Get the absolute value of the input number and convert it to an integer
    input_number = abs(int(input()))

    # Initialize a counter for natural numbers
    count = 0

    # Continuously search for a suitable count
    while True:
        # Calculate the sum of the first 'count' natural numbers
        sum_ = (count * (count + 1)) // 2

        # Calculate the difference between the sum and the input number
        difference = sum_ - input_number

        # Check if the sum exactly equals the input number
        if sum_ == input_number:
            print(count)  # Output the count
            break  # Exit the loop

        # Check if the sum is greater than the input number
        elif sum_ > input_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(count)  # Output the count
                break  # Exit the loop

        # Increment the count for the next iteration
        count += 1

find_count()
