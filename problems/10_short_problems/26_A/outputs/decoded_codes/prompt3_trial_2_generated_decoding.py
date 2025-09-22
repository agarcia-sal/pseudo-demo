def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read the total number of test cases
    total_test_cases = int(input())

    # Step 2: Initialize the result counter
    prime_count = 0

    # Step 3: Iterate over each number from 1 to total_test_cases
    for number in range(1, total_test_cases + 1):
        factor_count = 0
        current_number = number

        # Step 4: Check for factors starting from 2 to currentNumber-1
        for potential_factor in range(2, current_number):
            # Step 5: Check if potential_factor is a factor of current_number
            if current_number % potential_factor == 0:
                # Step 6: Increment factor_count for each valid factor found
                factor_count += 1

                # Step 7: Divide current_number by potentialFactor until it is no longer divisible
                while current_number % potential_factor == 0:
                    current_number //= potential_factor
                
            # Early exit if we found more than 2 distinct prime factors
            if factor_count > 2:
                break
        
        # Step 8: Check if the number has exactly 2 distinct prime factors
        if factor_count == 2:
            prime_count += 1

    # Step 9: Output the total count of numbers with exactly 2 distinct prime factors
    print(prime_count)

# Calling the function to execute
count_numbers_with_two_distinct_prime_factors()
