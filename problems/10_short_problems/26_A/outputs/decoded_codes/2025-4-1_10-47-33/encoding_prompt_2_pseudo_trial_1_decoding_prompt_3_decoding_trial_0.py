def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read the upper limit
    t = int(input())

    # Step 2: Initialize our result count
    result_count = 0

    # Step 3: Iterate through each number from 1 to t
    for current_number in range(1, t + 1):
        # Initialize factor count and current value
        factor_count = 0
        current_value = current_number

        # Step 4: Check for factors starting from 2 up to current_number - 1
        for potential_factor in range(2, current_number):
            if current_value % potential_factor == 0:  # found a factor
                factor_count += 1  # increment the factor count

                # Remove all instances of this factor from current_value
                while current_value % potential_factor == 0:
                    current_value //= potential_factor

        # Step 5: Check if we found exactly two distinct prime factors
        if factor_count == 2:
            result_count += 1  # Increment our result count

    # Step 6: Output the result
    print(result_count)

# Call the function to execute the program
count_numbers_with_two_distinct_prime_factors()
