def count_numbers_with_two_distinct_prime_factors(total_test_cases):
    # Initialize the result counter for numbers with exactly two distinct prime factors
    prime_count = 0

    for current_number in range(1, total_test_cases + 1):
        # Initialize a counter for the number of distinct prime factors
        distinct_prime_factors = 0
        
        # Copy the current number to a variable for factorization
        factorable_number = current_number

        # Check for factors starting from 2 up to the current number - 1
        for potential_factor in range(2, current_number):
            # Check if potential_factor is a divisor of factorable_number
            if factorable_number % potential_factor == 0:
                # Increment the distinct prime factors counter
                distinct_prime_factors += 1

                # Divide factorable_number by potential_factor until it no longer divides evenly
                while factorable_number % potential_factor == 0:
                    factorable_number //= potential_factor

        # Check if the number has exactly two distinct prime factors
        if distinct_prime_factors == 2:
            prime_count += 1

    # Return the total count of numbers with exactly two distinct prime factors
    return prime_count

# Read the total number of test cases
total_test_cases = int(input())
result = count_numbers_with_two_distinct_prime_factors(total_test_cases)

# Display the total count of numbers with exactly two distinct prime factors
print(result)
