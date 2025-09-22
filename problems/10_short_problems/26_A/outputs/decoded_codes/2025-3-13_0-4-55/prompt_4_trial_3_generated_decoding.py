def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_distinct_prime_factors(n):
    """Count the number of distinct prime factors of a number."""
    distinct_factors = 0
    number_to_check = n

    for potential_factor in range(2, n):
        if number_to_check % potential_factor == 0 and is_prime(potential_factor):
            distinct_factors += 1
            # Divide out all occurrences of this factor
            while number_to_check % potential_factor == 0:
                number_to_check //= potential_factor
    return distinct_factors

def main():
    # Read an integer input for the number of test cases
    number_of_test_cases = int(input())
    
    # Initialize the result counter for prime numbers
    prime_count = 0

    # Loop through each number from 1 to the specified number of test cases
    for current_number in range(1, number_of_test_cases + 1):
        # Count distinct prime factors for the current number
        if count_distinct_prime_factors(current_number) == 2:
            prime_count += 1

    # Output the total count of numbers that have exactly two distinct prime factors
    print(prime_count)

# Entry point of the program
if __name__ == "__main__":
    main()
