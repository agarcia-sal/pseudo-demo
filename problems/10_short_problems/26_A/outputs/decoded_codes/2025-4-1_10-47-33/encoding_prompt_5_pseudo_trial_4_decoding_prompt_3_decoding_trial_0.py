def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(limit):
    """Count how many numbers from 1 to limit are semiprime numbers."""
    semiprime_count = 0

    # Loop through each number from 1 to the limit (inclusive)
    for current_number in range(1, limit + 1):
        prime_factor_count = 0
        number_to_check = current_number

        # Check for prime factors
        for potential_prime in range(2, current_number):
            if number_to_check % potential_prime == 0:
                prime_factor_count += 1

                # Divide number_to_check until it's no longer divisible by potential_prime
                while number_to_check % potential_prime == 0:
                    number_to_check //= potential_prime

        # If there are exactly two prime factors, it's a semiprime
        if prime_factor_count == 2:
            semiprime_count += 1

    return semiprime_count

# Main execution
if __name__ == "__main__":
    limit = int(input())
    result = count_semiprimes(limit)
    print(result)
