def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_distinct_prime_products(input_number):
    """Count numbers between 1 and input_number that are products of exactly two distinct primes."""
    count_of_numbers = 0
    
    for current_number in range(1, input_number + 1):
        distinct_prime_count = 0
        working_number = current_number
        
        # Check for distinct prime factors
        for potential_factor in range(2, current_number):
            if working_number % potential_factor == 0 and is_prime(potential_factor):
                distinct_prime_count += 1
                
                # Divide out the prime factor completely
                while working_number % potential_factor == 0:
                    working_number //= potential_factor
        
        # Check if we found exactly two distinct primes
        if distinct_prime_count == 2:
            count_of_numbers += 1
    
    return count_of_numbers

# Read the input value
input_number = int(input())

# Get the count of numbers that are products of two distinct primes
result = count_distinct_prime_products(input_number)

# Output the result
print(result)
