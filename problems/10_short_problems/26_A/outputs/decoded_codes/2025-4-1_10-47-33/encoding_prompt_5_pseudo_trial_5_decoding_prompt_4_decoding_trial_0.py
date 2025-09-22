def count_primes():
    # Step 2: Read an integer value for the upper limit of the range.
    total_numbers = int(input())

    # Step 3: Initialize the prime count
    prime_count = 0

    # Step 4: Iterate over each number in the given range
    for current_number in range(1, total_numbers + 1):
        divisor_count = 0  # Count of divisors for the current number
        temp_number = current_number  # Temporary variable for checking divisibility

        # Step 5: Check for divisibility
        for potential_divisor in range(2, current_number):
            # Check if temp_number is divisible by potential_divisor
            if temp_number % potential_divisor == 0:
                divisor_count += 1  # Found a divisor
                # While the number is divisible, factor it out
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor

        # Step 6: Determine if current number is prime
        if divisor_count == 1:  # Only 1 divisor found (the number itself)
            prime_count += 1  # Increment the prime count

    # Step 7: Output the total count of prime numbers
    print(prime_count)

# Call the function to execute the counting of primes
count_primes()
