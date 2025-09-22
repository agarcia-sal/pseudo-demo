def is_prime(num):
    """Check if a given number is prime."""
    if num < 2:
        return False
    for potential_factor in range(2, int(num**0.5) + 1):
        if num % potential_factor == 0:
            return False
    return True

def count_primes_up_to(maximum_number):
    """Count the number of prime numbers up to a specified integer."""
    prime_count = 0
    for current_number in range(1, maximum_number + 1):
        if is_prime(current_number):
            prime_count += 1
    return prime_count

def main():
    # Get user input
    maximum_number = int(input())
    
    # Count and output the number of prime numbers
    prime_count = count_primes_up_to(maximum_number)
    print(prime_count)

if __name__ == "__main__":
    main()
