def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count the semiprimes up to the number t."""
    semiprime_count = 0

    for current_number in range(1, t + 1):
        factor_count = 0
        temp_number = current_number
        
        # Find distinct prime factors
        for possible_prime in range(2, current_number):
            if temp_number % possible_prime == 0 and is_prime(possible_prime):
                factor_count += 1
                
                # Reduce temp_number by dividing out possible_prime
                while temp_number % possible_prime == 0:
                    temp_number //= possible_prime

        # Check if the number is semiprime
        if factor_count == 2:
            semiprime_count += 1

    return semiprime_count

# Main execution
t = int(input())
result = count_semiprimes(t)
print(result)
