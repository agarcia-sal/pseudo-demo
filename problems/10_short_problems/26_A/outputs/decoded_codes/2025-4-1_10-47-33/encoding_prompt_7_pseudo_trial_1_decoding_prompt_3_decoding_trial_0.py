def count_semi_primes(limit):
    semi_prime_count = 0  # Counter for semi-primes

    for num in range(1, limit + 1):
        divisor_count = 0  # Counter for unique prime factors
        current_number = num
        
        # Check for divisors starting from 2 up to current_number - 1
        for divisor in range(2, current_number):
            if current_number % divisor == 0:  # Check if divisor is a factor
                divisor_count += 1  # Found a prime factor
                # Divide out all occurrences of this divisor
                while current_number % divisor == 0:
                    current_number //= divisor  # Reduce current number
            if divisor_count > 2:  # No need to count further if we exceed 2
                break
        
        # A semi-prime has exactly two unique prime factors
        if divisor_count == 2:
            semi_prime_count += 1  # Increase semi-prime count
    
    return semi_prime_count  # Output the count of semi-primes

# Main program execution
t = int(input())  # Get the limit for semi-prime count
print(count_semi_primes(t))  # Print the count of semi-primes up to t
