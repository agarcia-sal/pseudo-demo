def count_unique_prime_factors():
    # Read input
    t = int(input())

    # Initialize result count
    result_count = 0

    # Iterate through numbers from 1 to t inclusive
    for current_number in range(1, t + 1):
        unique_prime_factor_count = 0
        temp_number = current_number

        # Find unique prime factors
        for potential_prime in range(2, current_number):
            if temp_number % potential_prime == 0:  # Check if potential_prime is a factor
                unique_prime_factor_count += 1  # Found a new unique prime factor
                # Eliminate all instances of this prime factor from temp_number
                while temp_number % potential_prime == 0:
                    temp_number //= potential_prime

        # Check if we found exactly two unique prime factors
        if unique_prime_factor_count == 2:
            result_count += 1

    # Output the total count of numbers with exactly two unique prime factors
    print(result_count)

# Call the function
count_unique_prime_factors()
