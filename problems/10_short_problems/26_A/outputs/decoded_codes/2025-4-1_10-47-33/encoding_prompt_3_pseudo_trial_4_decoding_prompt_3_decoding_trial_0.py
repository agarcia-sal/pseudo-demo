def count_numbers_with_two_distinct_prime_factors():
    # Read the total number of test cases
    total_test_cases = int(input())
    
    # Initialize the result counter for numbers with exactly 2 distinct prime factors
    prime_count = 0
    
    # Loop through each number from 1 to total_test_cases
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
            # Increment the prime_count for each valid current_number
            prime_count += 1
    
    # Display the total count of numbers with exactly two distinct prime factors
    print(prime_count)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
