def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_distinct_prime_factors(n):
    """Count the number of distinct prime factors of n."""
    distinct_prime_factor_count = 0
    number_to_check = n
    
    # Check for factors from 2 to n-1
    for potential_factor in range(2, n):
        if number_to_check % potential_factor == 0 and is_prime(potential_factor):
            distinct_prime_factor_count += 1
            # Remove all occurrences of this prime factor
            while number_to_check % potential_factor == 0:
                number_to_check //= potential_factor
    return distinct_prime_factor_count

def main():
    # Read the number of test cases from input
    number_of_test_cases = int(input())
    
    # Initialize the result counter for numbers with exactly two distinct prime factors
    prime_count = 0

    # Loop through each number from 1 to the specified number of test cases
    for current_number in range(1, number_of_test_cases + 1):
        # Get the count of distinct prime factors for the current number
        if count_distinct_prime_factors(current_number) == 2:
            prime_count += 1
            
    # Output the total count of numbers that have exactly two distinct prime factors
    print(prime_count)

# Run the main function to execute the program
main()
