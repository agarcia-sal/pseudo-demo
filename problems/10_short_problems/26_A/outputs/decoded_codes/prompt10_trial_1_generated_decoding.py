def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read an integer input
    t = int(input())

    # Step 2: Initialize result counter
    result_count = 0

    # Step 3: Loop through numbers from 1 to t
    for i in range(1, t + 1):
        # Step 4: Initialize a count for prime factorization
        distinct_prime_factors_count = 0
        num = i

        # Step 5: Loop through potential factors from 2 to i-1
        for j in range(2, i):
            # Step 6: Check if j is a factor of num
            if num % j == 0:
                # Step 7: Increment the count of distinct prime factors
                distinct_prime_factors_count += 1

                # Step 8: Divide num by j as long as it is a factor
                while num % j == 0:
                    num //= j

        # Step 9: Check if exactly two distinct prime factors were found
        if distinct_prime_factors_count == 2:
            # Step 10: Increment the result counter for finding a number with exactly two distinct prime factors
            result_count += 1

    # Step 11: Print the total count of numbers with exactly two distinct prime factors
    print(result_count)

# Call the function to execute the program
count_numbers_with_two_distinct_prime_factors()
