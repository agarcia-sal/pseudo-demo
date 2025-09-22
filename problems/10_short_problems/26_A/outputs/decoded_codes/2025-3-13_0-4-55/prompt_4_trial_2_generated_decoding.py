def read_integer():
    return int(input())

def count_distinct_prime_factors(number):
    distinct_prime_count = 0
    potential_factor = 2
    original_number = number

    while potential_factor * potential_factor <= number:
        if number % potential_factor == 0:
            distinct_prime_count += 1
            while number % potential_factor == 0:
                number //= potential_factor
        potential_factor += 1
    
    if number > 1:  # This means number itself is a prime number larger than the square root
        distinct_prime_count += 1
    
    return distinct_prime_count

def main():
    # Read an integer input for the number of test cases
    number_of_test_cases = read_integer()

    # Initialize the result counter for prime numbers
    prime_count = 0

    # Loop through each number from 1 to the specified number of test cases
    for current_number in range(1, number_of_test_cases + 1):
        # Count distinct prime factors for the current number
        if count_distinct_prime_factors(current_number) == 2:
            prime_count += 1

    # Output the total count of numbers that have exactly two distinct prime factors
    print(prime_count)

if __name__ == "__main__":
    main()
