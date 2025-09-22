def count_semi_prime_numbers(input_number):
    # Initialize the count of semi-prime numbers
    semi_prime_count = 0
    
    # Check each integer from 1 to input_number
    for current_integer in range(1, input_number + 1):
        # Initialize the count of prime factors
        prime_factor_count = 0
        current_number = current_integer
        
        # Check for prime factors from 2 to current_integer - 1
        for factor in range(2, current_integer):
            if current_number % factor == 0:  # If factor is a prime factor
                prime_factor_count += 1  # Increment prime factor count
                
                # Divide current_number by factor until it's no longer divisible
                while current_number % factor == 0:
                    current_number //= factor
        
        # If the number has exactly 2 prime factors, it is a semi-prime
        if prime_factor_count == 2:
            semi_prime_count += 1  # Increment semi-prime count
    
    return semi_prime_count  # Return the total count of semi-prime numbers

# Example usage (you can uncomment and test):
# print(count_semi_prime_numbers(int(input())))
