def count_special_numbers():
    # Step 1: Initialize variable t as an integer input from the user.
    t = int(input())
    
    # Step 2: Initialize variable res to 0 to hold the count of special numbers.
    res = 0

    # Step 3: For each integer i from 1 to t (inclusive).
    for i in range(1, t + 1):
        # Step 3a: Initialize variable cnt to 0 to count the number of distinct prime factors of i.
        distinct_prime_factors_count = 0
        # Step 3b: Set variable num to i for factorization purposes.
        num = i

        # Step 4: For each integer j from 2 to i-1.
        for j in range(2, i):
            # Step 4a: Check if num is divisible by j.
            if num % j == 0:
                # Step 4ai: If yes, increment cnt by 1 (a new distinct factor found).
                distinct_prime_factors_count += 1
                # Step 4aii: While num is divisible by j.
                while num % j == 0:
                    # Step 4A: Divide num by j to factor out j completely.
                    num //= j

        # Step 5: After processing all j values, check if cnt equals 2.
        if distinct_prime_factors_count == 2:
            # Step 5a: If yes, increment res by 1 (i has exactly two distinct prime factors).
            res += 1

    # Step 6: After the loop ends, print the value of res.
    print(res)

# Function call to count the special numbers
count_special_numbers()
