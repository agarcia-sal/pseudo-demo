def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semi_primes(upper_limit):
    """Count the number of semi-prime numbers up to the upper limit."""
    semi_prime_count = 0

    for current_number in range(2, upper_limit + 1):
        prime_factor_count = 0
        factor_candidate = current_number

        for potential_factor in range(2, current_number):
            if factor_candidate % potential_factor == 0 and is_prime(potential_factor):
                prime_factor_count += 1
                
                # Factor out potential_factor completely
                while factor_candidate % potential_factor == 0:
                    factor_candidate //= potential_factor

        # A semi-prime number has exactly two distinct prime factors
        if prime_factor_count == 2:
            semi_prime_count += 1

    return semi_prime_count

# Read the upper limit from input
upper_limit = int(input())
# Call the function and print the result
print(count_semi_primes(upper_limit))
