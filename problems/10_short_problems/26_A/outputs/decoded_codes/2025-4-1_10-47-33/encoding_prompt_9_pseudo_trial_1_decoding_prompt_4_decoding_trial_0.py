def is_prime(num):
    """Check if a number is prime."""
    if num < 2:  # 0 and 1 are not prime numbers
        return False
    for potential_divisor in range(2, int(num**0.5) + 1):
        if num % potential_divisor == 0:
            return False
    return True

def count_primes(total):
    """Count the number of prime numbers up to a specified integer."""
    prime_count = 0  # Initialize count of prime numbers
    for current_number in range(1, total + 1):
        if is_prime(current_number):
            prime_count += 1  # Increment count if current_number is prime
    
    return prime_count

# Get the input from the user
total = int(input())  # Read an integer value representing the upper limit
prime_count = count_primes(total)  # Count the primes up to 'total'
print(prime_count)  # Output the prime count
