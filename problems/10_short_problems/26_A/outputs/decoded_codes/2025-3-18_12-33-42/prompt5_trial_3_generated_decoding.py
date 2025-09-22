def count_semiprimes():
    # Capture the total count of numbers to be checked
    total_numbers = int(input())
    
    # Initialize a counter for semiprime numbers
    semiprime_count = 0
    
    # Loop through each number from 1 to total_numbers
    for current_number in range(1, total_numbers + 1):
        
        # Initialize a counter for the number of distinct prime factors
        distinct_prime_factors = 0
        
        # Start with the current number to check for prime factors
        remaining_value = current_number
        
        # Loop through potential factors starting from 2 to current_number - 1
        for potential_factor in range(2, current_number):
            
            # Check if the potential factor is a divisor of remaining_value
            if remaining_value % potential_factor == 0:
                
                # Increment the count of distinct prime factors
                distinct_prime_factors += 1
                
                # Divide remaining_value by potential_factor until it is no longer divisible
                while remaining_value % potential_factor == 0:
                    remaining_value //= potential_factor
                
            # If we already found two distinct prime factors, we can break early
            if distinct_prime_factors > 2:
                break
        
        # After checking all factors, check if we found exactly two prime factors
        if distinct_prime_factors == 2:
            # Increment the count of semiprime numbers
            semiprime_count += 1
    
    # Output the total count of semiprime numbers found
    print(semiprime_count)

# Example test case (Uncomment to test)
# count_semiprimes() 
