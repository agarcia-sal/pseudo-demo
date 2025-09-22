def count_integers_with_two_prime_factors():
    # Step 1: Read the total number of integers to check for prime factors
    total_count = int(input())

    # Step 2: Initialize result variable to count specific integers
    specific_prime_count = 0

    # Step 3: Loop through each integer from 1 to total_count
    for current_integer in range(1, total_count + 1):
        
        # Step 4: Initialize counter for prime factors
        prime_factor_count = 0
        number = current_integer
        
        # Step 5: Check for prime factors starting from 2 up to current_integer
        for potential_factor in range(2, current_integer):
            
            # Step 6: Check if potential_factor is a divisor of number
            if number % potential_factor == 0:
                
                # Increase the prime factor counter
                prime_factor_count += 1
                
                # Step 7: Divide number by potentialFactor until it's no longer divisible
                while number % potential_factor == 0:
                    number //= potential_factor
                    
        # Step 8: Check if exactly two distinct prime factors were found
        if prime_factor_count == 2:
            # Increment the count of integers with exactly two prime factors
            specific_prime_count += 1
    
    # Step 9: Output the final count of integers with exactly two distinct prime factors
    print(specific_prime_count)

# Call the function to execute
count_integers_with_two_prime_factors()
