def count_numbers_with_two_distinct_prime_factors():
    # Read an integer input for the number of test cases
    number_of_test_cases = int(input())
    
    # Initialize the result counter for numbers with two distinct prime factors
    number_count_with_two_primes = 0
    
    # Loop through each number from 1 to the specified number of test cases
    for current_number in range(1, number_of_test_cases + 1):
        # Initialize a counter for the number of distinct prime factors
        distinct_prime_factor_count = 0
        number_to_check = current_number
        
        # Check for factors from 2 up to the current number
        for potential_factor in range(2, current_number):
            # If potential_factor is a divisor of number_to_check
            if number_to_check % potential_factor == 0:
                # Increment the distinct prime factor count
                distinct_prime_factor_count += 1
                
                # Reduce number_to_check by dividing it by potential_factor repeatedly
                while number_to_check % potential_factor == 0:
                    number_to_check //= potential_factor

        # If there are exactly two distinct prime factors, we count this number
        if distinct_prime_factor_count == 2:
            number_count_with_two_primes += 1
    
    # Output the total count of numbers that have exactly two distinct prime factors
    print(number_count_with_two_primes)

# Run the function to execute the logic
count_numbers_with_two_distinct_prime_factors()
