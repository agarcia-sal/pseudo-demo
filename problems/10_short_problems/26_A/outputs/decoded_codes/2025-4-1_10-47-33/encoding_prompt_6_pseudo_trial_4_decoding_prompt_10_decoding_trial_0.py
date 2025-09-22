def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    unique_prime_factors_count = 0
    
    # Check potential prime factors from 2 to num - 1
    for potential_prime_factor in range(2, num):
        if num % potential_prime_factor == 0:
            unique_prime_factors_count += 1
            
            # Divide num by potential_prime_factor until it's no longer divisible
            while num % potential_prime_factor == 0:
                num //= potential_prime_factor
                
        # If more than two unique prime factors, break early
        if unique_prime_factors_count > 2:
            return False

    return unique_prime_factors_count == 2

def count_primes(upper_limit):
    """Count the number of prime numbers up to `upper_limit`."""
    prime_count = 0

    # Loop through each number from 1 to upper_limit
    for number in range(1, upper_limit + 1):
        if is_prime(number):
            prime_count += 1

    return prime_count

# Main execution
if __name__ == "__main__":
    upper_limit = int(input())
    result = count_primes(upper_limit)
    print(result)
