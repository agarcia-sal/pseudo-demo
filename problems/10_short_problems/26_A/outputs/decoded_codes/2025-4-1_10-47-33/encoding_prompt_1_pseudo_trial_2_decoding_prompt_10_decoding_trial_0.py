def count_numbers_with_two_distinct_prime_factors(test_cases):
    result = 0  # Initialize the result to count numbers with exactly two distinct prime factors

    for num in range(1, test_cases + 1):
        count_of_distinct_primes = 0
        current_number = num

        # Check for divisibility starting from 2 up to current_number - 1
        for potential_prime in range(2, current_number):
            if current_number % potential_prime == 0:  # If divisible, it's a factor
                count_of_distinct_primes += 1
                
                # Remove all occurrences of the prime factor from current_number
                while current_number % potential_prime == 0:
                    current_number //= potential_prime
                    
        # Increment result if there are exactly two distinct prime factors
        if count_of_distinct_primes == 2:
            result += 1

    return result  # Return the final count of numbers with exactly two distinct prime factors

# Main execution block
if __name__ == "__main__":
    t = int(input())  # Read the total number of test cases
    result_count = count_numbers_with_two_distinct_prime_factors(t)  # Get the result
    print(result_count)  # Output the result
