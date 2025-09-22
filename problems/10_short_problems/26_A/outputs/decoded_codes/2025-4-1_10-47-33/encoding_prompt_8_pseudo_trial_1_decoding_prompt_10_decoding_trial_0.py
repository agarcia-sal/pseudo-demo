def count_numbers_with_two_distinct_prime_factors():
    # Read the total count from user input
    total_count = int(input())
    
    # Initialize a counter for numbers with exactly two distinct prime factors
    count_of_numbers_with_two_distinct_prime_factors = 0

    # Loop through each number from 1 to total_count (inclusive)
    for current_number in range(1, total_count + 1):
        distinct_prime_factors_count = 0  # Count of distinct prime factors for the current number
        working_number = current_number      # Store the current number to modify during factorization
        
        # Check for prime factors
        for potential_factor in range(2, current_number):
            if working_number % potential_factor == 0:
                # Found a prime factor, increment the count
                distinct_prime_factors_count += 1
                
                # Eliminate all occurrences of this prime factor from working_number
                while working_number % potential_factor == 0:
                    working_number //= potential_factor
        
        # Check if the current number has exactly two distinct prime factors
        if distinct_prime_factors_count == 2:
            count_of_numbers_with_two_distinct_prime_factors += 1

    # Output the final count
    print(count_of_numbers_with_two_distinct_prime_factors)

# Execute the function to start the program
count_numbers_with_two_distinct_prime_factors()
