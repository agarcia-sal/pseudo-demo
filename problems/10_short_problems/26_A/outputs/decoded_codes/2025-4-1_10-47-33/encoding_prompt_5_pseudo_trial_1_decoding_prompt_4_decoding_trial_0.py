def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(upper_limit):
    """Count semiprime numbers from 1 to the upper limit."""
    semiprime_count = 0

    for number in range(1, upper_limit + 1):
        prime_factor_count = 0
        current_number = number

        for potential_factor in range(2, current_number):
            if current_number % potential_factor == 0:
                prime_factor_count += 1

                while current_number % potential_factor == 0:
                    current_number //= potential_factor

        if prime_factor_count == 2:
            semiprime_count += 1

    return semiprime_count

# Main execution
upper_limit = int(input())
result = count_semiprimes(upper_limit)
print(result)
