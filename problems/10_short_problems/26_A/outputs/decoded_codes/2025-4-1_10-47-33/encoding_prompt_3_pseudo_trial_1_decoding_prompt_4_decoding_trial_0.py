def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semi_primes(limit):
    """Count semi-prime numbers up to the given limit."""
    total_semi_primes = 0
    
    for current_number in range(1, limit + 1):
        divisor_count = 0
        temp_number = current_number
        
        # Find prime factors
        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0 and is_prime(potential_divisor):
                divisor_count += 1
                
                # Reduce temp_number by the prime factor
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
        
        # Check for semi-prime condition
        if divisor_count == 2:
            total_semi_primes += 1

    return total_semi_primes

# Accepting input
t = int(input())
# Output the result
print(count_semi_primes(t))
