def count_numbers_with_two_distinct_prime_factors():
    # Read the number of test cases or range limit
    test_case_count = int(input())

    # Initialize a variable to hold the result
    result_count = 0

    # Loop through each number from 1 to the test case count (inclusive)
    for number in range(1, test_case_count + 1):
        # Initialize a counter for the number of distinct prime factors
        distinct_prime_factor_count = 0
        current_number = number

        # Loop through potential factors starting from 2 up to the current number
        for potential_factor in range(2, number):
            # Check if the potential factor divides the current number evenly
            if current_number % potential_factor == 0:
                # Increase the count of distinct prime factors
                distinct_prime_factor_count += 1
                
                # Divide the current number by the factor as long as it's divisible
                while current_number % potential_factor == 0:
                    current_number //= potential_factor

            # If we have already found two distinct prime factors, we can break early
            if distinct_prime_factor_count > 2:
                break

        # Check if the current number had exactly two distinct prime factors
        if distinct_prime_factor_count == 2:
            result_count += 1

    # Output the total count of numbers with exactly two distinct prime factors
    print(result_count)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
