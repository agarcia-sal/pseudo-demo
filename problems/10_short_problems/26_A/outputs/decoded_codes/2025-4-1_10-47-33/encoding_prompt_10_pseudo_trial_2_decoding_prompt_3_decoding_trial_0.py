def count_numbers_with_two_prime_factors():
    # Step 1: Read the input value
    t = int(input())  # User input as an integer

    # Step 2: Initialize result counter
    res = 0

    # Step 3: Loop through each integer from 1 to t
    for i in range(1, t + 1):
        # Step 4: Initialize prime factor counter
        cnt = 0
        num = i  # Store current value of i in num

        # Step 5: Check for factors of num
        for j in range(2, i):
            if num % j == 0:  # Check if j is a factor of num
                cnt += 1  # Increment count of prime factors

                # Step 6: Remove all occurrences of the factor j from num
                while num % j == 0:
                    num //= j

        # Step 7: Check if the count of prime factors equals 2
        if cnt == 2:
            # Step 8: Increment the result counter for each valid i
            res += 1

    # Step 9: Output the result
    print(res)

# Call the function to execute
count_numbers_with_two_prime_factors()
