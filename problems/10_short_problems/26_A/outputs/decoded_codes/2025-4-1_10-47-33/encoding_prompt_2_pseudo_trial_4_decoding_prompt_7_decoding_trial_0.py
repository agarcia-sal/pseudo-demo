# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Input: Read an integer value `t` which represents the upper limit
    t = int(input())
    
    # Initialize: Set a variable `result` to 0 for counting numbers
    result = 0 

    # Loop through numbers from 1 to `t` (inclusive)
    for current_number in range(1, t + 1):
        # Initialize factor count for the current number
        factor_count = 0
        # Set a temporary number to the current number being analyzed
        temp_number = current_number
        
        # Check for factors starting from 2 up to one less than current_number
        for potential_factor in range(2, current_number):
            # If `temp_number` is divisible by `potential_factor`
            if temp_number % potential_factor == 0:
                # Found a new distinct prime factor
                factor_count += 1
                # Remove all occurrences of this factor from `temp_number`
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
            
            # If we already found 2 distinct prime factors, we can break early
            if factor_count > 2:
                break
        
        # After checking all potential factors for current_number
        if factor_count == 2:
            # Increment the result as we found a number with exactly two distinct prime factors
            result += 1
    
    # Output: Print the total count of numbers found
    print(result)

# Call the function to execute the logic
count_numbers_with_two_distinct_prime_factors()
