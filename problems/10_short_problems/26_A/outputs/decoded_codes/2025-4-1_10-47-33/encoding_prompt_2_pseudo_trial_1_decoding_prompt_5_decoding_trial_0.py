# Function to count the number of integers with exactly two distinct prime factors
def count_numbers_with_two_prime_factors():
    # Read an integer value that serves as the upper limit
    upper_limit = int(input())
    
    # Initialize a counter for the result
    result_count = 0
    
    # Iterate through each integer from 1 to upper_limit
    for current_number in range(1, upper_limit + 1):
        # Initialize count for distinct prime factors
        factor_count = 0
        # Set a value to manipulate for factor extraction
        current_value = current_number
        
        # Check potential factors starting from 2 up to current_number - 1
        for potential_factor in range(2, current_number):
            # Check if the potential_factor is a factor of current_value
            if current_value % potential_factor == 0:
                # Found a new distinct prime factor
                factor_count += 1
                # Remove all instances of this factor from current_value
                while current_value % potential_factor == 0:
                    current_value //= potential_factor
        
        # Check if the current_number has exactly two distinct prime factors
        if factor_count == 2:
            result_count += 1  # Increment the result count
    
    # Output the total count of integers with exactly two distinct prime factors
    print(result_count)

# Call the function to execute
count_numbers_with_two_prime_factors()
