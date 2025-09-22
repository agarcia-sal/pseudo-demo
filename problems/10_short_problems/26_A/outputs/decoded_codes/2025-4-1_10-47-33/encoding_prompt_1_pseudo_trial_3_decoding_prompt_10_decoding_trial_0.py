def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_of_semi_primes(limit):
    """Count the number of semi-prime numbers up to a given limit."""
    semi_prime_count = 0
    
    for i in range(1, limit + 1):
        count_divisors = 0
        current_number = i
        
        # Check each number from 2 to i-1
        for j in range(2, i):
            if current_number % j == 0 and is_prime(j):
                count_divisors += 1
                
                # Factor out all occurrences of j
                while current_number % j == 0:
                    current_number //= j
        
        # Check if we have exactly 2 distinct prime factors
        if count_divisors == 2:
            semi_prime_count += 1
            
    return semi_prime_count

# Read input
t = int(input())
# Call the function and print the result
result = count_of_semi_primes(t)
print(result)
