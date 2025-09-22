def count_numbers_with_two_distinct_prime_factors():
    # Read upper limit for checking numbers
    upper_limit = int(input())
    result_count = 0  # Counter for numbers with exactly two distinct prime factors

    # Loop through each number from 1 to upper_limit
    for current_number in range(1, upper_limit + 1):
        distinct_prime_factors_count = 0  # Reset count for distinct prime factors
        temp_number = current_number  # Temporary variable for factorization

        # Check for potential factors from 2 to current_number - 1
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:  # If potential_factor is a factor
                distinct_prime_factors_count += 1  # Found a new distinct prime factor
                # Divide temp_number by potential_factor to remove all occurrences
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # After checking all potential factors
        if distinct_prime_factors_count == 2:  # Check if exactly 2 distinct prime factors
            result_count += 1  # Increment the result count

    # Output the total count of numbers with exactly two distinct prime factors
    print(result_count)

# Example test case
# count_numbers_with_two_distinct_prime_factors()

