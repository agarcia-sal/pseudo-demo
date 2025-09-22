def count_semi_primes():
    # Step 1: Read the input value for the number of test cases
    number_of_test_cases = int(input())
    
    # Step 2: Initialize a variable to store the count of semi-prime numbers
    semi_prime_count = 0

    # Step 3: Loop through each number from 1 to the number of test cases
    for current_number in range(1, number_of_test_cases + 1):
        # Step 4: Initialize a counter for distinct prime factors
        distinct_prime_factors = 0
        factor_candidate = current_number

        # Step 5: Check for prime factors from 2 up to one less than the current number
        for potential_factor in range(2, current_number):
            # Step 6: If the potential factor divides the current number
            if factor_candidate % potential_factor == 0:
                # Increment the count of distinct prime factors
                distinct_prime_factors += 1
                
                # Step 7: Remove all occurrences of this factor from the current number
                while factor_candidate % potential_factor == 0:
                    factor_candidate //= potential_factor
        
        # Step 8: If the count of distinct prime factors is exactly two
        if distinct_prime_factors == 2:
            # It is a semi-prime, increment the overall count
            semi_prime_count += 1

    # Step 9: Output the total count of semi-prime numbers found
    print(semi_prime_count)

# Example call to the function
count_semi_primes()
