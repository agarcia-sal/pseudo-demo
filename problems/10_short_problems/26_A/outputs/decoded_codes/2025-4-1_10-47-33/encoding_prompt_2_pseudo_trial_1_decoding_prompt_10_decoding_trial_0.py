def count_numbers_with_two_distinct_prime_factors(t):
    result_count = 0  # Initialize result count

    # Iterate through each number from 1 to t
    for current_number in range(1, t + 1):
        factor_count = 0  # Reset factor count for each number
        current_value = current_number  # Store the current number to manipulate

        # Check potential factors from 2 up to current_number - 1
        for potential_factor in range(2, current_number):
            if current_value % potential_factor == 0:  # Check if it's a factor
                factor_count += 1  # Increment factor count
                
                # Remove all instances of this factor from current_value
                while current_value % potential_factor == 0:
                    current_value //= potential_factor
                
        # Check if the count of distinct prime factors is exactly 2
        if factor_count == 2:
            result_count += 1  # Increment result count for valid numbers

    return result_count  # Return the total count


# Read user input for the upper limit t
t = int(input())
# Call the function and print the result
print(count_numbers_with_two_distinct_prime_factors(t))
