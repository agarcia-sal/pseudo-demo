def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_semiprimes(limit):
    """Count the number of semiprime numbers up to a given limit."""
    semiprime_count = 0

    for current_number in range(1, limit + 1):
        prime_factor_count = 0
        temp_number = current_number

        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0 and is_prime(potential_factor):
                prime_factor_count += 1
                # Divide temp_number by potential_factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        # Check if the number has exactly two prime factors
        if prime_factor_count == 2:
            semiprime_count += 1

    return semiprime_count

if __name__ == "__main__":
    # Read limit from user input
    limit = int(input())
    semiprime_count = count_semiprimes(limit)
    print(semiprime_count)
