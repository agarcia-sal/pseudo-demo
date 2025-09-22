def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semiprimes(upper_limit):
    """Count the number of semiprime numbers up to the given upper limit."""
    semiprime_count = 0

    for current_number in range(1, upper_limit + 1):
        prime_factor_count = 0
        divided_number = current_number
        
        # Check for prime factors
        for possible_factor in range(2, current_number):
            if divided_number % possible_factor == 0 and is_prime(possible_factor):
                prime_factor_count += 1
                while divided_number % possible_factor == 0:
                    divided_number //= possible_factor
        
        # Check for the semiprime condition
        if prime_factor_count == 2:
            semiprime_count += 1

    return semiprime_count

# Receiving user input
upper_limit = int(input())
semiprime_count = count_semiprimes(upper_limit)
print(semiprime_count)
