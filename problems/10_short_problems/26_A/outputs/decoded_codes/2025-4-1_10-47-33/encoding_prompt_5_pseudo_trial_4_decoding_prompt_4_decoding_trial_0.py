def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(limit):
    """Count the number of semiprime numbers up to a given limit."""
    semiprime_count = 0
    
    for current_number in range(1, limit + 1):
        prime_factor_count = 0
        number_to_check = current_number
        
        for potential_prime in range(2, current_number):
            if number_to_check % potential_prime == 0:
                prime_factor_count += 1
                while number_to_check % potential_prime == 0:
                    number_to_check //= potential_prime
                    
        if prime_factor_count == 2:
            semiprime_count += 1
            
    return semiprime_count

# Read limit from user
limit = int(input())
result = count_semiprimes(limit)
print(result)
