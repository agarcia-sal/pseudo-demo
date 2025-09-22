def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read an integer value from the user
    total_count = int(input())
    
    # Step 2: Initialize a result variable
    count_of_numbers_with_two_distinct_prime_factors = 0

    # Step 3: Loop through each number from 1 to total_count (inclusive)
    for current_number in range(1, total_count + 1):
        distinct_prime_factors_count = 0
        working_number = current_number

        # Step 3.1: Check for prime factors
        for potential_factor in range(2, working_number):  # Checking factors from 2 to (current_number-1)
            if working_number % potential_factor == 0:  # Found a factor
                distinct_prime_factors_count += 1
                
                # Remove all occurrences of this prime factor
                while working_number % potential_factor == 0:
                    working_number //= potential_factor

        # Step 3.2: Check for exactly two distinct factors
        if distinct_prime_factors_count == 2:
            count_of_numbers_with_two_distinct_prime_factors += 1

    # Step 4: Output the result
    print(count_of_numbers_with_two_distinct_prime_factors)

# Call the function to execute the code
count_numbers_with_two_distinct_prime_factors()
