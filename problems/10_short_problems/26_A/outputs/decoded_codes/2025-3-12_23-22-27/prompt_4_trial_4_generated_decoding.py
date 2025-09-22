def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_distinct_prime_factors(num):
    """Count the number of distinct prime factors of a number."""
    prime_factors = set()
    # Check for factors from 2 up to the current number
    for potential_factor in range(2, num + 1):
        while num % potential_factor == 0:  # While potential_factor is a divisor of num
            prime_factors.add(potential_factor)
            num //= potential_factor
        if num == 1:  # No need to check further if fully divided
            break
    return len(prime_factors)

def main():
    # Read an integer input for the number of test cases
    number_of_test_cases = int(input())
    
    # Initialize the result counter for prime numbers
    prime_count = 0

    # Loop through each number from 1 to the specified number of test cases
    for current_number in range(1, number_of_test_cases + 1):
        distinct_prime_factor_count = count_distinct_prime_factors(current_number)
        # Increment prime_count if current_number has exactly 2 distinct prime factors
        if distinct_prime_factor_count == 2:
            prime_count += 1

    # Output the total count of numbers that have exactly two distinct prime factors
    print(prime_count)

if __name__ == "__main__":
    main()
