def is_prime(number):
    """Determine if the provided number is a prime number."""
    if number < 2:
        return False
    divisor_count = 0
    
    # Check for divisibility from 2 to number - 1
    for potential_divisor in range(2, number):
        if number % potential_divisor == 0:
            divisor_count += 1
            
        # Early exit if more than 2 divisors found
        if divisor_count > 2:
            return False
            
    return divisor_count == 1  # Only 1 divisor (the number itself) makes it prime

def count_primes(limit):
    """Count the number of prime numbers up to the specified limit."""
    prime_count = 0
    
    for current_number in range(1, limit + 1):
        if is_prime(current_number):
            prime_count += 1
    
    return prime_count

def main():
    """Main function to execute the prime counting algorithm."""
    total = int(input())  # Get the upper limit from the user
    prime_count = count_primes(total)  # Count the prime numbers
    print(prime_count)  # Output the result

if __name__ == "__main__":
    main()
