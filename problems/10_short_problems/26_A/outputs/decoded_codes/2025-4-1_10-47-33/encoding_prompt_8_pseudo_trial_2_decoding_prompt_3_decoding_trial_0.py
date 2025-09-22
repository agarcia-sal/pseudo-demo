def count_semiprimes():
    # Step 1: Read an integer value called 'limit' from user input.
    limit = int(input())
    
    # Step 2: Initialize a variable 'semiprimeCount' to track semiprime numbers.
    semiprime_count = 0

    # Step 3: Iterate through each number from 1 to 'limit' (inclusive).
    for current_number in range(1, limit + 1):
        prime_factor_count = 0  # Count of prime factors for the current number.
        temp_number = current_number  # Copy of the current number for factorization.

        # Step 3c: Check potential factors starting from 2.
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:  # If divisible by potential factor.
                prime_factor_count += 1

                # Step 3c ii: Reduce temp_number by the prime factor.
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor  # Remove the factor completely.

        # Step 4: Check if the number of prime factors is exactly 2.
        if prime_factor_count == 2:
            semiprime_count += 1  # Increment semiprime count for valid semiprimes.

    # Output the total number of semiprime numbers found.
    print(semiprime_count)

# Run the semiprime counting function
count_semiprimes()
