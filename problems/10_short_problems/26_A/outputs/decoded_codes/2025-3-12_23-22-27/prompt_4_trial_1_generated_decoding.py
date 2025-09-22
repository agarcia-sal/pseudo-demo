def is_prime(num):
    """Helper function to determine if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_distinct_prime_factors(number):
    """Count distinct prime factors of a given number."""
    distinct_count = 0
    original_number = number
    
    for potential_factor in range(2, original_number):
        if number % potential_factor == 0:
            # If potential_factor is a divisor, check if it is prime
            if is_prime(potential_factor):
                distinct_count += 1
                # Divide the number by potential_factor until it no longer divides
                while number % potential_factor == 0:
                    number //= potential_factor
    return distinct_count

# Read input for the number of test cases
number_of_test_cases = int(input())

# Initialize the result counter for numbers with exactly two distinct prime factors
prime_count = 0

# Loop through each number from 1 to the specified number of test cases
for current_number in range(1, number_of_test_cases + 1):
    if count_distinct_prime_factors(current_number) == 2:
        prime_count += 1

# Output the total count of numbers that have exactly two distinct prime factors
print(prime_count)
