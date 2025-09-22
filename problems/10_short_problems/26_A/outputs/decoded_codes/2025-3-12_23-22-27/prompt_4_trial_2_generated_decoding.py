def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_distinct_prime_factors(number):
    """Count the distinct prime factors of a given number."""
    count = 0
    potential_factor = 2
    while potential_factor <= number:
        if number % potential_factor == 0:
            count += 1
            while number % potential_factor == 0:
                number //= potential_factor
        potential_factor += 1
    return count

def main():
    # Read the number of test cases
    number_of_test_cases = int(input())
    
    # Initialize the result counter for numbers with exactly two distinct prime factors
    prime_count = 0

    # Loop through each number from 1 to the specified number of test cases
    for current_number in range(1, number_of_test_cases + 1):
        distinct_prime_factor_count = count_distinct_prime_factors(current_number)
        
        # Check if the count of distinct prime factors is exactly 2
        if distinct_prime_factor_count == 2:
            prime_count += 1

    # Output the total count of numbers that have exactly two distinct prime factors
    print(prime_count)

# Call the main function to execute the program
main()
