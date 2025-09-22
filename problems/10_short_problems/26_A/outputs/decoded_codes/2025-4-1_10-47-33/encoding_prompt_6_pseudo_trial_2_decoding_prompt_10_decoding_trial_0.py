def count_special_numbers():
    # Read total numbers to evaluate
    total_numbers = int(input())

    # Initialize the count of special numbers
    count_of_special_numbers = 0

    # Loop through each number from 1 to total_numbers
    for current_number in range(1, total_numbers + 1):
        divisor_count = 0  # Count of unique divisors for the current number
        current_value = current_number  # Current value to check for divisors

        # Check for divisors from 2 to current_number - 1
        for divisor in range(2, current_number):
            if current_value % divisor == 0:  # Check if divisor is a factor
                divisor_count += 1  # We found a unique divisor

                # Remove all instances of this divisor from current_value
                while current_value % divisor == 0:
                    current_value //= divisor

        # Check if we have exactly two unique divisors
        if divisor_count == 2:
            count_of_special_numbers += 1  # Increment count of special numbers

    # Print the final count of special numbers
    print(count_of_special_numbers)

# Call the function to execute
count_special_numbers()
