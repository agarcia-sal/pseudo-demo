def count_numbers_with_two_unique_prime_factors(upper_limit):
    # Initialize a counter for the results
    prime_count = 0

    # Iterate from 1 to the upper limit
    for number in range(1, upper_limit + 1):
        factor_count = 0
        current_number = number

        # Check for factors from 2 up to the current number
        for potential_factor in range(2, current_number):
            # If current_number is divisible by potential_factor
            if current_number % potential_factor == 0:
                factor_count += 1
                
                # Divide current_number by potential_factor until it can no longer be done
                while current_number % potential_factor == 0:
                    current_number //= potential_factor

        # Check if the number has exactly two unique prime factors
        if factor_count == 2:
            prime_count += 1

    # Print the total count of numbers with exactly two unique prime factors
    print(prime_count)

# Read the integer input representing the upper limit
upper_limit = int(input())
count_numbers_with_two_unique_prime_factors(upper_limit)
