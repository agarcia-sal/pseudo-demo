def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Initialize the total number of test cases
    t = int(input())
    
    # Step 2: Initialize result count
    result = 0

    # Step 3: Iterate over each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        count_of_distinct_primes = 0  # To count distinct prime factors
        current_number = i

        # Step 3.3: Check for prime factors starting from 2
        for j in range(2, current_number):  # Check divisors up to current_number - 1
            if current_number % j == 0:  # If j is a factor
                count_of_distinct_primes += 1  # Found a distinct prime factor
                
                # Factor out all occurrences of j
                while current_number % j == 0:
                    current_number //= j

        # Step 4: If exactly two distinct prime factors are found, increment result
        if count_of_distinct_primes == 2:
            result += 1

    # Output the final count of numbers with exactly two distinct prime factors
    print(result)

# Invoke the function
count_numbers_with_two_distinct_prime_factors()
