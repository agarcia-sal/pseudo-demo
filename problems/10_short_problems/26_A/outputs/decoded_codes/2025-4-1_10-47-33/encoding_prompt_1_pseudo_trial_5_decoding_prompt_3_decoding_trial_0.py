def count_numbers_with_two_distinct_prime_factors():
    # Read an integer input which represents the upper limit for checking numbers
    t = int(input())
    
    # Initialize counter for numbers with exactly two distinct prime factors
    result_count = 0
    
    # Loop through each number from 1 to t
    for current_number in range(1, t + 1):
        # Initialize counter for distinct prime factors
        distinct_prime_factors_count = 0
        temp_number = current_number # Number to be factorized
        
        # Check for potential prime factors starting from 2
        for potential_factor in range(2, current_number):
            # Check if potential_factor is a factor of temp_number
            if temp_number % potential_factor == 0:
                distinct_prime_factors_count += 1
                
                # Eliminate all occurrences of this prime factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # Check if we have exactly two distinct prime factors
        if distinct_prime_factors_count == 2:
            result_count += 1
    
    # Output the count of numbers with exactly two distinct prime factors
    print(result_count)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
