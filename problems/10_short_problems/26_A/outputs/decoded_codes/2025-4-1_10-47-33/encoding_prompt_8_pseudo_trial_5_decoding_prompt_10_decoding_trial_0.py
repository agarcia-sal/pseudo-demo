def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_numbers_with_two_distinct_primes(input_number):
    """Count how many numbers between 1 and input_number are products of exactly two distinct prime numbers."""
    count_of_numbers = 0
    
    # Iterate over each number from 1 to input_number
    for current_number in range(1, input_number + 1):
        distinct_prime_count = 0
        working_number = current_number
        
        # Check for prime factors from 2 to current_number - 1
        for potential_factor in range(2, current_number):
            if working_number % potential_factor == 0 and is_prime(potential_factor):
                distinct_prime_count += 1
                
                # Remove all instances of this prime factor
                while working_number % potential_factor == 0:
                    working_number //= potential_factor
        
        # Check if we exactly have two distinct prime factors
        if distinct_prime_count == 2:
            count_of_numbers += 1
            
    return count_of_numbers

# Read the input value
input_number = int(input())

# Get the count of numbers with exactly two distinct prime factors
result = count_numbers_with_two_distinct_primes(input_number)

# Output the result
print(result)
