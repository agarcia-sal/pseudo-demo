def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read the total number of test cases.
    t = int(input())
    # Step 2: Initialize result to count numbers with exactly two distinct prime factors.
    result = 0

    # Step 3: Iterate through each number from 1 to t (inclusive).
    for i in range(1, t + 1):
        count_of_distinct_primes = 0  # Count distinct prime factors.
        current_number = i  # The number to be factored.

        # Step 3.3: Check potential divisors from 2 to i-1.
        for j in range(2, i):
            if current_number % j == 0:  # j is a divisor of current_number.
                count_of_distinct_primes += 1  # Found a new prime factor.
                
                # Step 3.3.2: Factor out j completely.
                while current_number % j == 0:
                    current_number //= j
            
            # If we already found two distinct prime factors, break early for efficiency.
            if count_of_distinct_primes > 2:
                break

        # Step 4: Check if we have exactly two distinct prime factors.
        if count_of_distinct_primes == 2:
            result += 1  # Increment the count of valid numbers.

    # Output the final result.
    print(result)

# Uncomment the line below to run the function when you're ready.
# count_numbers_with_two_distinct_prime_factors()
