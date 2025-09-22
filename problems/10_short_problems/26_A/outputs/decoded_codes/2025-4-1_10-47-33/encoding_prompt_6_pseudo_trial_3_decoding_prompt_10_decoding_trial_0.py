def count_numbers_with_two_unique_prime_factors(limit):
    """Counts how many numbers from 1 to 'limit' have exactly two unique prime factors."""
    
    # Initialize a variable to keep track of the count of numbers with exactly two unique prime factors
    count_with_two_prime_factors = 0

    # Loop through each number from 1 to limit (inclusive)
    for current_number in range(1, limit + 1):
        # Initialize a counter to track the number of unique prime factors for the current number
        unique_prime_factors_count = 0
        
        # Check for potential prime factors starting from 2 up to current_number // 2
        for potential_factor in range(2, current_number // 2 + 1):
            # If potential_factor is a factor of current_number
            if current_number % potential_factor == 0:
                unique_prime_factors_count += 1
                
                # Divide current_number by potential_factor until it is no longer divisible by potential_factor
                while current_number % potential_factor == 0:
                    current_number //= potential_factor
        
        # After checking all factors, if the count of unique prime factors is exactly 2
        if unique_prime_factors_count == 2:
            count_with_two_prime_factors += 1

    return count_with_two_prime_factors


# Read an integer input that represents the upper limit for checking prime numbers
t = int(input())

# Call the function and print the total count of numbers with exactly two unique prime factors
result = count_numbers_with_two_unique_prime_factors(t)
print(result)
