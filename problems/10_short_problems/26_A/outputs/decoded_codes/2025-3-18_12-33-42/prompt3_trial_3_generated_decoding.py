def count_primes():
    # Input: Read an integer from the user
    num_count = int(input())

    # Initialize variable to store the count of prime numbers
    prime_count = 0

    # Loop through each integer from 1 to num_count (inclusive)
    for current_number in range(1, num_count + 1):
        # Initialize a variable to count the number of distinct prime factors
        distinct_prime_factors = 0
        
        # Temporary variable to work with current_number
        temp_number = current_number
        
        # Check for factors starting from 2 to one less than current_number
        for potential_factor in range(2, current_number):
            # If potential_factor is a divisor of temp_number
            if temp_number % potential_factor == 0:
                # Increment the count of distinct prime factors
                distinct_prime_factors += 1
                
                # Divide temp_number by potential_factor until it is no longer divisible
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # A prime number must have exactly two distinct prime factors (1 and itself)
        if distinct_prime_factors == 1 and current_number > 1:
            # Increment the prime count
            prime_count += 1
            
    # Output: Print the total count of prime numbers found
    print(prime_count)

# Test the function
count_primes()
