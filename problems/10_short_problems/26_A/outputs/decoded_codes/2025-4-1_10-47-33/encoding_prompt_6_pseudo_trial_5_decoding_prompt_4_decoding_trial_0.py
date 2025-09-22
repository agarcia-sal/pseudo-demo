def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Input the upper limit t from the user
    t = int(input())

    # Step 2: Initialize the result counter
    total_count = 0

    # Step 3: Loop through each number from 1 to t
    for current_number in range(1, t + 1):
        distinct_prime_count = 0  # Count distinct prime factors
        current_value = current_number  # Value to be factored

        # Step 4: Find prime factors
        for potential_prime in range(2, current_number):  # Check potential primes
            if current_value % potential_prime == 0:  # Check divisibility
                distinct_prime_count += 1  # Found a new distinct prime
                # Remove all occurrences of potential_prime from current_value
                while current_value % potential_prime == 0:
                    current_value //= potential_prime
        
        # Step 5: Check if the count of distinct primes is exactly 2
        if distinct_prime_count == 2:
            total_count += 1  # Increment total count if exactly 2 distinct primes

    # Step 6: Output the result
    print(total_count)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
