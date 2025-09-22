def count_numbers_with_two_distinct_prime_factors():
    # Read the total count of numbers to check
    total_count = int(input())
    
    # Initialize the result counter
    result = 0
    
    # Loop through each number from 1 to total_count (inclusive)
    for current_number in range(1, total_count + 1):
        # Counter for distinct prime factors
        distinct_prime_count = 0
        # Temporary number to work with
        temp_number = current_number
        
        # Find prime factors
        for potential_factor in range(2, current_number):
            # Check if temp_number is divisible by potential_factor
            if temp_number % potential_factor == 0:
                # Found a new distinct prime factor
                distinct_prime_count += 1
                
                # Eliminate all occurrences of potential_factor from temp_number
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
                    
            # Exit early if we already found 2 distinct primes
            if distinct_prime_count > 2:
                break
        
        # Count numbers with exactly two distinct primes
        if distinct_prime_count == 2:
            result += 1
    
    # Output the result
    print(result)

# Example of calling the function
count_numbers_with_two_distinct_prime_factors()
