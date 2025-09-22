def is_prime(number):
    """Determine if a number is prime."""
    if number <= 1:
        return False
    for potential_divisor in range(2, int(number**0.5) + 1):
        if number % potential_divisor == 0:
            return False
    return True

def count_primes(total_numbers):
    """Count prime numbers from 1 to total_numbers."""
    prime_count = 0
    for current_number in range(1, total_numbers + 1):
        if is_prime(current_number):
            prime_count += 1
    return prime_count

def main():
    """Main function to execute the program."""
    total_numbers = int(input())
    prime_count = count_primes(total_numbers)
    print(prime_count)

if __name__ == "__main__":
    main()
