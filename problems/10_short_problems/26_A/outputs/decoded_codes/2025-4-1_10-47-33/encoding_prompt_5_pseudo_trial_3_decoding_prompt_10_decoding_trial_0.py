def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def semiprime_count(t):
    """Count semiprime numbers from 1 to t."""
    semiprime_count = 0

    for current_number in range(1, t + 1):
        factor_count = 0
        temp_number = current_number
        
        # Check for prime factors
        for possible_prime in range(2, current_number):
            if temp_number % possible_prime == 0:
                factor_count += 1
                
                # Reduce temp_number by possible_prime
                while temp_number % possible_prime == 0:
                    temp_number //= possible_prime
        
        # A number is a semiprime if it has exactly two distinct prime factors
        if factor_count == 2:
            semiprime_count += 1
            
    return semiprime_count

def main():
    t = int(input())
    result = semiprime_count(t)
    print(result)

if __name__ == "__main__":
    main()
