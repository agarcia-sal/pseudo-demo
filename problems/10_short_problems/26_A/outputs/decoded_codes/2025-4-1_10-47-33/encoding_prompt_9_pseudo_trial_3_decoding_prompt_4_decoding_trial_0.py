def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for potential_factor in range(2, int(number**0.5) + 1):
        if number % potential_factor == 0:
            return False
    return True

def count_semiprimes(t):
    """Count the number of semiprime numbers up to t."""
    semiprime_count = 0
    
    for current_number in range(2, t + 1):  # Semiprimes start from 4
        distinct_prime_count = 0
        number = current_number
        
        for potential_factor in range(2, current_number):
            if number % potential_factor == 0 and is_prime(potential_factor):
                distinct_prime_count += 1
                while number % potential_factor == 0:
                    number //= potential_factor
        
        if distinct_prime_count == 2:
            semiprime_count += 1
            
    return semiprime_count

if __name__ == '__main__':
    # Read user input
    t = int(input())
    result = count_semiprimes(t)
    print(result)
