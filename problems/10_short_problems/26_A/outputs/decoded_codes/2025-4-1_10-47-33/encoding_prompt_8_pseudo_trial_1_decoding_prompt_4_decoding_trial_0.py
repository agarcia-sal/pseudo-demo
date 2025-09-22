def count_numbers_with_two_distinct_prime_factors():
    # Read an integer value from the user
    total_count = int(input())
    
    # Initialize a result variable
    count_of_numbers_with_two_distinct_prime_factors = 0

    # Loop through each number from 1 to total_count (inclusive)
    for current_number in range(1, total_count + 1):
        distinct_prime_factors_count = 0
        working_number = current_number
        
        # Check for prime factors
        for potential_factor in range(2, current_number):
            if working_number % potential_factor == 0:  # Check if potential_factor is a divisor
                distinct_prime_factors_count += 1
                # Remove all instances of this prime factor
                while working_number % potential_factor == 0:
                    working_number //= potential_factor

        # Check if there are exactly two distinct prime factors
        if distinct_prime_factors_count == 2:
            count_of_numbers_with_two_distinct_prime_factors += 1

    # Output the result
    print(count_of_numbers_with_two_distinct_prime_factors)

# Call the function to execute the program
count_numbers_with_two_distinct_prime_factors()
