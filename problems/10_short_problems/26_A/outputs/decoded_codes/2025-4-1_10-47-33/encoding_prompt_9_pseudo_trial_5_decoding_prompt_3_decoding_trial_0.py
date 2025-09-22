def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count the semiprime numbers up to a given limit t."""
    semiprime_count = 0
    
    # Loop through each number from 1 to t
    for current_number in range(1, t + 1):
        prime_factor_count = 0
        divided_number = current_number
        
        # Identify prime factors for the current number
        for possible_factor in range(2, current_number):
            if divided_number % possible_factor == 0:
                prime_factor_count += 1
                
                # Keep dividing out the prime factor
                while divided_number % possible_factor == 0:
                    divided_number //= possible_factor
                    
            # If we already found 2 prime factors, we can stop checking
            if prime_factor_count > 2:
                break
        
        # Check for semiprime condition
        if prime_factor_count == 2:
            semiprime_count += 1
    
    return semiprime_count

# Get user input
t = int(input())
# Count and print semiprimes
print(count_semiprimes(t))
