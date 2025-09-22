def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for potential_prime in range(2, int(n**0.5) + 1):
        if n % potential_prime == 0:
            return False
    return True

def count_products_of_two_distinct_primes(limit):
    """Count numbers up to 'limit' that are products of exactly two distinct prime numbers."""
    count_of_products = 0

    for current_number in range(1, limit + 1):
        distinct_prime_factors = 0
        temporary_number = current_number
        
        for potential_prime in range(2, current_number):
            if is_prime(potential_prime) and temporary_number % potential_prime == 0:
                distinct_prime_factors += 1
                # Divide out all occurrences of this prime factor
                while temporary_number % potential_prime == 0:
                    temporary_number //= potential_prime
        
        if distinct_prime_factors == 2:
            count_of_products += 1

    return count_of_products

# Main program
limit = int(input())
result = count_products_of_two_distinct_primes(limit)
print(result)
