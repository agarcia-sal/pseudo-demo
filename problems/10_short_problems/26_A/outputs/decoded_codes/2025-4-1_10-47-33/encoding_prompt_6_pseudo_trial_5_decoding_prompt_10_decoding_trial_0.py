def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_numbers_with_two_distinct_prime_factors(t):
    """Count numbers from 1 to t that have exactly two distinct prime factors."""
    total_count = 0
    
    for current_number in range(1, t + 1):
        distinct_prime_count = 0
        current_value = current_number
        
        for potential_prime in range(2, current_number):
            if current_value % potential_prime == 0 and is_prime(potential_prime):
                distinct_prime_count += 1
                # Divide out all multiples of potential_prime
                while current_value % potential_prime == 0:
                    current_value //= potential_prime
        
        if distinct_prime_count == 2:
            total_count += 1
            
    return total_count

# Input from the user
t = int(input())
result = count_numbers_with_two_distinct_prime_factors(t)
print(result)
