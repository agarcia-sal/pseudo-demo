def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semi_primes(t):
    """Count semi-prime numbers up to a given integer t."""
    total_semi_primes = 0
    
    for current_number in range(1, t + 1):
        divisor_count = 0
        temp_number = current_number
        
        # Find distinct prime factors
        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0 and is_prime(potential_divisor):
                divisor_count += 1
                
                # Reduce temp_number by this prime factor
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
            
            # Early exit if we already found more than 2 distinct prime factors
            if divisor_count > 2:
                break
        
        # Check if we have exactly two distinct prime factors
        if divisor_count == 2:
            total_semi_primes += 1
            
    return total_semi_primes

# Example input
t = int(input())
result = count_semi_primes(t)
print(result)
