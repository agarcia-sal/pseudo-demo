def count_numbers_with_two_prime_factors():
    # Step 1: Read an integer input representing the maximum limit (t)
    limit = int(input())

    # Step 2: Initialize a counter for the result
    prime_count = 0

    # Step 3: Iterate through all numbers from 1 to the limit (inclusive)
    for number in range(1, limit + 1):
        # Initialize a divisor count and a variable to keep track of the current number
        divisor_count = 0
        current_number = number

        # Step 4: Check for divisors from 2 to one less than the current number
        for potential_divisor in range(2, current_number):
            # Check if potential_divisor is a divisor of current_number
            while current_number % potential_divisor == 0:
                current_number //= potential_divisor
                # Count the divisor only once for each distinct prime factor
                if current_number % potential_divisor == 0:
                    divisor_count += 1
                # If the current_number reduces to 1, we can break the loop
                if current_number == 1:
                    break

        # Step 6: Check if exactly two distinct prime factors were found
        if divisor_count == 2:
            prime_count += 1  # Found a number with exactly two prime factors

    # Step 7: Print the total count of numbers with exactly two prime factors
    print(prime_count)

# Test the function by calling it
count_numbers_with_two_prime_factors()
