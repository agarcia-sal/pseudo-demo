def count_numbers_with_two_prime_factors():
    # Step 1: Initialize variables
    t = int(input())  # Number of test cases
    res = 0  # Result counter

    # Step 2: Loop through each number from 1 to t
    for i in range(1, t + 1):
        cnt = 0  # Count of distinct prime factors
        num = i  # Current number to check

        # Step 3: Check for factors of the current number
        for j in range(2, i):  # Check for factors from 2 to i-1
            if num % j == 0:  # If j is a factor of num
                cnt += 1  # Increment the count of distinct prime factors
                
                # Step 4: Divide num by j as long as it's divisible
                while num % j == 0:  # Reduce num while j is a factor
                    num //= j

        # Step 5: Check if the number has exactly two prime factors
        if cnt == 2:  # If there are exactly two distinct prime factors
            res += 1  # Increment the result counter

    # Step 6: Output the result
    print(res)

# Call the function
count_numbers_with_two_prime_factors()
