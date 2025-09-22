def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_semiprimes(upper_limit):
    """Count the number of semiprime numbers up to a specified upper limit."""
    semiprime_count = 0  # Counter for semiprime numbers

    for number in range(1, upper_limit + 1):
        prime_factor_count = 0  # Count of distinct prime factors
        current_number = number  # Number being evaluated

        for potential_factor in range(2, current_number):  # Iterate potential factors
            if current_number % potential_factor == 0:  # Check if divisible
                prime_factor_count += 1  # Found a new distinct prime factor
                
                # Continuously divide current_number by potential_factor
                while current_number % potential_factor == 0:
                    current_number //= potential_factor

        # Check if exactly two distinct prime factors were found
        if prime_factor_count == 2:
            semiprime_count += 1  # Found a semiprime number

    return semiprime_count

def main():
    # Take an integer input for the upper limit
    upper_limit = int(input())
    
    # Get the count of semiprimes and print the result
    semiprime_count = count_semiprimes(upper_limit)
    print(semiprime_count)

if __name__ == "__main__":
    main()
