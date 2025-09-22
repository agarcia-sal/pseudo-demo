def count_numbers_with_two_distinct_prime_factors():
    # Read an integer value t from input
    t = int(input())
    
    # Initialize result to hold the count of numbers with two distinct prime factors
    result = 0
    
    # Loop through each number from 1 to t (inclusive)
    for current_number in range(1, t + 1):
        factor_count = 0  # Count of distinct prime factors for current_number
        temp_number = current_number  # Use a temporary variable to factorize
        
        # Check for prime factors starting from 2
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:  # Found a factor
                factor_count += 1  # Increment factor count
                # Remove all occurrences of potential_factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # After checking all factors, check if we have exactly two distinct prime factors
        if factor_count == 2:
            result += 1  # Increment result if current_number meets condition
    
    # Output the total count of numbers with exactly two distinct prime factors
    print(result)

# Execute the function
count_numbers_with_two_distinct_prime_factors()
