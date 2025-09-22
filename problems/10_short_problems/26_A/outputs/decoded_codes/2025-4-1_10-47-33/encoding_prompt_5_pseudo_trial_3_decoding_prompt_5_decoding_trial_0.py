def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semiprimes(t):
    """Count how many semiprimes are in the range from 1 to t."""
    semiprime_count = 0
    
    for current_number in range(1, t + 1):
        factor_count = 0
        temp_number = current_number

        # Find prime factors
        for possible_prime in range(2, current_number):
            if temp_number % possible_prime == 0:  # found a divisor
                factor_count += 1
                
                # Reduce the number by dividing it by the found prime
                while temp_number % possible_prime == 0:
                    temp_number //= possible_prime

        # Check for semiprime (exactly two distinct prime factors)
        if factor_count == 2:
            semiprime_count += 1

    return semiprime_count

# Get input from the user
t = int(input())
# Count and print the semiprimes
print(count_semiprimes(t))
