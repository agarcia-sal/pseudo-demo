def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for potential_factor in range(2, int(n ** 0.5) + 1):
        if n % potential_factor == 0:
            return False
    return True

def count_primes(test_case_count):
    """Count prime numbers from 1 to test_case_count."""
    prime_count = 0
    
    for current_number in range(1, test_case_count + 1):
        if is_prime(current_number):
            prime_count += 1
            
    return prime_count

def main():
    # Get the number of test cases from user input
    test_case_count = int(input())
    
    # Count and print the number of prime numbers
    prime_count = count_primes(test_case_count)
    print(prime_count)

if __name__ == "__main__":
    main()
