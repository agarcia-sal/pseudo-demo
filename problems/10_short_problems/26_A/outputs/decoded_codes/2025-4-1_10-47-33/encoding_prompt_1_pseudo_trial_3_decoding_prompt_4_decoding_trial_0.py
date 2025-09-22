def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semi_primes(t):
    """Count the number of semi-prime numbers up to a given integer t."""
    result = 0

    # We need to find the semi-primes which are products of exactly two primes
    for i in range(2, t + 1):
        count_divisors = 0
        current_number = i
        
        # Check for all numbers possible as prime factors
        for j in range(2, current_number):
            if current_number % j == 0 and is_prime(j):
                count_divisors += 1
                # Factor out all occurrences of the prime factor j
                while current_number % j == 0:
                    current_number //= j
                    
            # If we find two distinct prime factors, we can break early
            if count_divisors > 2:
                break
                
        # A semi-prime must have exactly two distinct prime factors
        if count_divisors == 2:
            result += 1

    return result

# Main routine to get input and call the function
t = int(input())
semi_prime_count = count_semi_primes(t)
print(semi_prime_count)
