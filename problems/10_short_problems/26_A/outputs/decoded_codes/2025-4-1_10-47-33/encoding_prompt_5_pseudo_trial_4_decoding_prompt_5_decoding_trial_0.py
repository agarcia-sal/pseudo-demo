def count_semiprimes():
    # Read the upper limit from the user
    limit = int(input())
    
    # Initialize the count of semiprimes
    semiprime_count = 0

    # Loop through all numbers from 1 to the limit
    for current_number in range(1, limit + 1):
        # Initialize prime factor count for the current number
        prime_factor_count = 0
        number_to_check = current_number
        
        # Find prime factors of the current number
        for potential_prime in range(2, current_number):
            if number_to_check % potential_prime == 0:  # Check divisibility
                prime_factor_count += 1  # Found a prime factor
                
                # Divide number_to_check by potential_prime until it's no longer divisible
                while number_to_check % potential_prime == 0:
                    number_to_check //= potential_prime
        
        # Check if the current number is semiprime
        if prime_factor_count == 2:
            semiprime_count += 1  # Increment semiprime count if two prime factors found
            
    # Output the total count of semiprime numbers found
    print(semiprime_count)

# Example of how to call the function for testing
# count_semiprimes()
