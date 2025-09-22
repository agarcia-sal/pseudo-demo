# Function to count numbers from 1 to timePeriod that have exactly two distinct prime factors
def count_numbers_with_two_prime_factors():
    # Read user input
    time_period = int(input())  # Get the total count of numbers to examine
    result_count = 0  # Initialize the count of valid numbers

    # Loop through each number from 1 to time_period
    for current_number in range(1, time_period + 1):
        divisor_count = 0  # Initialize the count of distinct divisors
        temp_number = current_number  # Work with a temporary copy of current_number

        # Check for potential divisors from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0:  # Check if divisible
                divisor_count += 1  # Increment the divisor count
                # Divide temp_number by potential_divisor until it's no longer divisible
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
        
        # If exactly two distinct prime factors were found
        if divisor_count == 2:
            result_count += 1  # Increment the result count

    # Print the total count of numbers with exactly two distinct prime factors
    print(result_count)

# Example usage
# count_numbers_with_two_prime_factors()
