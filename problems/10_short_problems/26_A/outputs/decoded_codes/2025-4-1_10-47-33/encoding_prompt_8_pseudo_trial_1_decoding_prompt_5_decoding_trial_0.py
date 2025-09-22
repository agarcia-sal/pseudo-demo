# Function to count how many numbers from 1 to totalCount
# are exactly the product of two distinct prime factors.
def count_numbers_with_two_distinct_prime_factors():
    # Read an integer value from the user
    total_count = int(input())
    
    # Initialize a variable to hold the count of desired numbers
    count_of_numbers_with_two_distinct_prime_factors = 0
    
    # Loop through each number from 1 to totalCount (inclusive)
    for current_number in range(1, total_count + 1):
        # Initialize the count of distinct prime factors
        distinct_prime_factors_count = 0
        # Initialize working number for factorization
        working_number = current_number
        
        # Check for prime factors
        for potential_factor in range(2, current_number):
            # Check if potential_factor is a divisor of working_number
            if working_number % potential_factor == 0:
                # Increment the distinct prime factor count
                distinct_prime_factors_count += 1
                
                # Remove all occurrences of this prime factor from working_number
                while working_number % potential_factor == 0:
                    working_number //= potential_factor
        
        # Check if we found exactly two distinct prime factors
        if distinct_prime_factors_count == 2:
            count_of_numbers_with_two_distinct_prime_factors += 1
    
    # Output the result
    print(count_of_numbers_with_two_distinct_prime_factors)

# Example of how to call the function (Note: Uncomment to test)
# count_numbers_with_two_distinct_prime_factors()
