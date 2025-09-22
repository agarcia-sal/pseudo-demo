def count_semi_prime_numbers():
    # Get user input
    input_number = int(input())
    
    # Initialize result for counting semi-primes
    result = 0
    
    # Iterate through each integer from 1 to input_number
    for current_integer in range(1, input_number + 1):
        prime_factor_count = 0
        current_number = current_integer
        
        # Check for prime factors from 2 up to current_integer - 1
        for factor in range(2, current_integer):
            if current_number % factor == 0:  # Check if factor is a prime factor
                prime_factor_count += 1
                
                # Divide current_number by factor until it no longer can
                while current_number % factor == 0:
                    current_number //= factor
                    
            # If we already found two prime factors, break early
            if prime_factor_count > 2:
                break
        
        # Check if the count of prime factors is exactly 2
        if prime_factor_count == 2:
            result += 1  # Increment the count of semi-prime numbers
    
    return result
