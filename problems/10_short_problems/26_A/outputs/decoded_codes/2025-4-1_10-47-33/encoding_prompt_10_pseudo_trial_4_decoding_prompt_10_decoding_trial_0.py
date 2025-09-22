def count_numbers_with_distinct_prime_factors():
    # Step 1: Input the number of test cases
    t = int(input())

    # Step 2: Initialize the result counter
    res = 0  # This will hold the count of numbers with exactly two distinct prime factors

    # Step 3: Loop through each number from 1 to t
    for i in range(1, t + 1):
        cnt = 0  # This will count the number of distinct prime factors
        num = i  # Set num to the current number to factorize

        # Step 4: Loop to find factors
        for j in range(2, i):
            # Check if j is a factor of num
            if num % j == 0:
                cnt += 1  # Found a new prime factor
                # Remove all occurrences of this prime factor from num
                while num % j == 0:
                    num //= j

        # Step 5: Check for prime condition
        if cnt == 2:  # Verify that the current number i has exactly two distinct prime factors
            res += 1  # Count this number as valid

    # Step 6: Output the result
    print(res)  # Total count of numbers with exactly two distinct prime factors

# Call the function to execute the program 
count_numbers_with_distinct_prime_factors()
