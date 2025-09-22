def count_numbers_with_two_distinct_prime_factors():
    # Input the number
    total_count = int(input())

    # Initialize a result counter
    result = 0

    # Loop through each number from 1 to total_count (inclusive)
    for current_number in range(1, total_count + 1):
        distinct_prime_count = 0  # Counter for distinct prime factors
        temp_number = current_number  # Working copy of current_number

        # Find prime factors
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:
                distinct_prime_count += 1  # Found a prime factor
                
                # Divide out all occurrences of this prime factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
            
            # Early exit if we already found more than two distinct primes
            if distinct_prime_count > 2:
                break

        # Count numbers with exactly two distinct primes
        if distinct_prime_count == 2:
            result += 1

    # Output the result
    print(result)

# Execute the function
count_numbers_with_two_distinct_prime_factors()
