def count_numbers_with_two_distinct_prime_factors():
    # Read input for the upper limit
    t = int(input())
    
    # Initialize the result count to zero
    result_count = 0
    
    # Iterate through each number from 1 to t
    for current_number in range(1, t + 1):
        factor_count = 0          # Counter for distinct prime factors
        current_value = current_number  # Value to check for factors
        
        # Check potential factors starting from 2
        for potential_factor in range(2, current_number):
            # If potential_factor is a factor of current_value
            if current_value % potential_factor == 0:
                factor_count += 1  # New distinct factor found

                # Remove all instances of potential_factor from current_value
                while current_value % potential_factor == 0:
                    current_value //= potential_factor

        # Check if we found exactly two distinct prime factors
        if factor_count == 2:
            result_count += 1  # Increment the result count

    # Output the total count of integers with exactly two distinct prime factors
    print(result_count)

# Function call to execute the program
count_numbers_with_two_distinct_prime_factors()
