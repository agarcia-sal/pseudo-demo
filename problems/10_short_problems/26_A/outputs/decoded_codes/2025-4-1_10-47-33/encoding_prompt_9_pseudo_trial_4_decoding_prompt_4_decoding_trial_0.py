def count_products_of_two_distinct_primes():
    # Start Program
    
    # Step 2: Receive Input
    limit = int(input())  # Read positive integer input
    
    # Step 3: Initialize Count
    count_of_products = 0  # Initialize the count of valid products found

    # Step 4: Iterate Through Numbers
    for current_number in range(1, limit + 1):
        distinct_prime_factors = 0  # Track distinct prime factors for current number
        temporary_number = current_number  # Work on a copy of the current number
        
        # Step 5: Check for Prime Factors
        for potential_prime in range(2, current_number):
            if temporary_number % potential_prime == 0:  # Check if it's a prime factor
                distinct_prime_factors += 1  # Found a new distinct prime factor
                
                # Remove all occurrences of the prime factor
                while temporary_number % potential_prime == 0:
                    temporary_number //= potential_prime
        
        # Step 6: Check the Condition
        if distinct_prime_factors == 2:  # Check for exactly two distinct prime factors
            count_of_products += 1  # Increment the count

    # Step 7: Output Result
    print(count_of_products)  # Output the result

# Step 8: End Program
count_products_of_two_distinct_primes()
