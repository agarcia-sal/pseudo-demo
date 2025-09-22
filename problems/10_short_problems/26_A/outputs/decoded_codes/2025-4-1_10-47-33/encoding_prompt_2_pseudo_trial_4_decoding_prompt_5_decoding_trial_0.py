# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Read the upper limit for checking numbers
    upper_limit = int(input())
    
    # Initialize result to hold the count of specific numbers
    result = 0

    # Loop through numbers from 1 to upper_limit (inclusive)
    for current_number in range(1, upper_limit + 1):
        # Initialize factor_count to count distinct prime factors
        factor_count = 0
        # Make a temporary variable to manipulate
        temp_number = current_number
        
        # Check for potential factors starting from 2
        for potential_factor in range(2, current_number):
            # If potential_factor is a factor of temp_number
            if temp_number % potential_factor == 0:
                # Found a new distinct prime factor
                factor_count += 1
                # Divide out all occurrences of the factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # Count the number if it has exactly two distinct prime factors
        if factor_count == 2:
            result += 1

    # Print the total count of numbers with exactly two distinct prime factors
    print(result)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
