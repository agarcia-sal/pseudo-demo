def count_numbers_with_two_prime_factors(test_cases):
    # Initialize the result counter to zero
    result_count = 0

    # Iterate through each number from 1 to the number of test cases
    for i in range(1, test_cases + 1):
        # Initialize a counter for prime factors
        prime_factor_count = 0
        num = i
        
        # Check for factors from 2 to one less than the number
        for j in range(2, i):
            if num % j == 0:  # If num is divisible by j
                prime_factor_count += 1  # Increment the prime factor counter
                
                # Divide num by j until it is no longer divisible
                while num % j == 0:
                    num //= j  # Use integer division to avoid float errors

        # If the number has exactly two distinct prime factors
        if prime_factor_count == 2:
            result_count += 1  # Increment the result count

    # Output the total count of numbers with exactly two prime factors
    return result_count


# Read the integer input for the number of test cases
test_cases = int(input())
# Call the function and print the result
print(count_numbers_with_two_prime_factors(test_cases))
