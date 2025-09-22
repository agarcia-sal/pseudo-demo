def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_products_of_two_distinct_primes(limit):
    """Count numbers that are products of exactly two distinct prime numbers up to a given limit."""
    count_of_products = 0
    
    for current_number in range(1, limit + 1):
        distinct_prime_factors = 0
        temporary_number = current_number
        
        # Check for prime factors from 2 to current_number - 1
        for potential_prime in range(2, current_number):
            if temporary_number % potential_prime == 0 and is_prime(potential_prime):
                distinct_prime_factors += 1
                
                # Remove this prime factor from temporary_number
                while temporary_number % potential_prime == 0:
                    temporary_number //= potential_prime
        
        # Check if we have exactly two distinct prime factors
        if distinct_prime_factors == 2:
            count_of_products += 1

    return count_of_products

def main():
    """Main function to execute the program."""
    limit = int(input())
    result = count_products_of_two_distinct_primes(limit)
    print(result)

if __name__ == "__main__":
    main()
