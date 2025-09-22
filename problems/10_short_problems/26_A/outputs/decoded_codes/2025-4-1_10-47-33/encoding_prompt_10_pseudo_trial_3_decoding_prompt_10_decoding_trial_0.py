def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True

def count_primes(t):
    """Count numbers from 1 to t that have exactly two distinct prime factors."""
    prime_count = 0
    
    for i in range(1, t + 1):
        factor_count = 0
        num = i
        
        # Check each number from 2 to num's square root for factors
        for j in range(2, num + 1):
            if num % j == 0 and is_prime(j):
                factor_count += 1
                # Remove all occurrences of this prime factor
                while num % j == 0:
                    num //= j
            
            # If we have already found 2 distinct prime factors, we can stop
            if factor_count > 2:
                break
        
        # Increment prime_count if exactly 2 distinct prime factors found
        if factor_count == 2:
            prime_count += 1
            
    return prime_count

def main():
    """Main function to execute the program."""
    t = int(input())
    result = count_primes(t)
    print(result)

if __name__ == "__main__":
    main()
