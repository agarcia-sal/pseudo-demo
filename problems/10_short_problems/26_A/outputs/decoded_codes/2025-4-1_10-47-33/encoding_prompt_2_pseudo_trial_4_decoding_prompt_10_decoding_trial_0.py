def count_numbers_with_two_distinct_prime_factors(t):
    """
    Count the integers from 1 to t that have exactly two distinct prime factors.

    Parameters:
    t (int): The upper limit for checking numbers.

    Returns:
    int: The count of numbers with exactly two distinct prime factors.
    """
    result = 0  # Initialize the count of numbers with two distinct prime factors.

    # Loop through each number from 1 to t (inclusive).
    for current_number in range(1, t + 1):
        factor_count = 0  # Reset factor count for the current number.
        temp_number = current_number  # Make a copy of the current number for factorization.

        # Check for potential factors from 2 to less than current_number.
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:  # Check if it is a factor.
                factor_count += 1  # Found a new distinct prime factor.

                # Remove all occurrences of this factor from temp_number.
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        # After checking all potential factors, check if we found exactly 2.
        if factor_count == 2:
            result += 1  # Increment the result count.

    return result  # Return the final count.


if __name__ == "__main__":
    t = int(input())  # Read integer input for t.
    print(count_numbers_with_two_distinct_prime_factors(t))  # Output the result.
