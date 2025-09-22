def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Get the upper limit from user input
    t = int(input())

    # Step 2: Initialize counter for numbers with exactly two distinct prime factors
    res = 0

    # Step 3: Loop through each number from 1 to t
    for i in range(1, t + 1):
        cnt = 0  # Count of distinct prime factors
        num = i  # Number to check for prime factors
        
        # Check for factors from 2 up to i-1
        for j in range(2, i):
            if num % j == 0:  # j is a factor of num
                cnt += 1  # Found a prime factor
                # Reduce num by factor j until it no longer divides evenly
                while num % j == 0:
                    num //= j  # Integer division to find next prime factor
        
        # Check if we found exactly 2 distinct prime factors
        if cnt == 2:
            res += 1  # Increment result counter
            
    # Step 4: Output the result
    print(res)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
