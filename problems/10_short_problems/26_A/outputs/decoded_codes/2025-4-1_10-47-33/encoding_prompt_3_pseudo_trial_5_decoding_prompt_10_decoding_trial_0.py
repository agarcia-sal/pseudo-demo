def count_numbers_with_exactly_two_prime_factors(time_period):
    result_count = 0  # Initialize the result count to track numbers with exactly two prime factors

    for current_number in range(1, time_period + 1):
        divisor_count = 0  # Count of distinct prime factors for current_number
        temp_number = current_number  # Create a working copy of the current number

        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0:  # Check if potential_divisor is a factor
                divisor_count += 1  # Found a new prime factor
                while temp_number % potential_divisor == 0:  # Remove all occurrences of this factor
                    temp_number //= potential_divisor
        
        if divisor_count == 2:  # Check if we found exactly two distinct prime factors
            result_count += 1  # Increment result count for the current number

    print(result_count)  # Output the total count


# Read input for time period
time_period = int(input())

# Call the function to execute the logic
count_numbers_with_exactly_two_prime_factors(time_period)
