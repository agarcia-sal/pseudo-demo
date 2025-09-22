def is_prime(number):
    """Returns True if the number is a prime, False otherwise."""
    if number <= 1:
        return False
    for potential_factor in range(2, int(number**0.5) + 1):
        if number % potential_factor == 0:
            return False
    return True

def count_primes(maximum_number):
    """Counts the number of prime numbers up to the specified maximum number."""
    prime_count = 0
    for current_number in range(1, maximum_number + 1):
        if is_prime(current_number):
            prime_count += 1
    return prime_count

def main():
    """Main function to execute the prime counting."""
    maximum_number = int(input())
    total_primes = count_primes(maximum_number)
    print(total_primes)

if __name__ == "__main__":
    main()
