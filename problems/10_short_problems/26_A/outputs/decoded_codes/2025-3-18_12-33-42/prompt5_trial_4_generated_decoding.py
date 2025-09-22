# Function to count semiprime numbers
def count_semiprimes():
    # Get the total number from user input
    total_numbers = int(input())
    semiprime_count = 0  # Initialize count of semiprime numbers

    # Loop through each number from 1 to total_numbers (inclusive)
    for current_number in range(1, total_numbers + 1):
        distinct_prime_count = 0  # Reset the prime factor count for the current number
        remaining_number = current_number  # Keep track of the number being factorized

        # Check for potential prime factors
        for potential_factor in range(2, current_number):  # Check factors from 2 to current_number - 1
            if remaining_number % potential_factor == 0:  # If divisible by potential_factor
                distinct_prime_count += 1  # Found a new distinct prime factor
                # Remove all occurrences of potential_factor from remaining_number
                while remaining_number % potential_factor == 0:
                    remaining_number //= potential_factor

        # Check if the current number is semiprime (exactly 2 distinct prime factors)
        if distinct_prime_count == 2:
            semiprime_count += 1  # Increment count of semiprimes

    # Output the total count of semiprime numbers found
    print(semiprime_count)

# Example test case
# It will prompt for input. E.g., if the user enters 10, it will count semiprimes from 1 to 10.
