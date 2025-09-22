def count_prime_numbers():
    # Step 1: Read the input value
    t = int(input())

    # Step 2: Initialize result counter
    result_count = 0

    # Step 3: Loop through each integer from 1 to t
    for i in range(1, t + 1):
        # Step 4: Initialize prime factor counter
        prime_factor_count = 0
        num = i  # Store current value of i in num

        # Step 5: Check for factors of num
        for j in range(2, i):
            # Check if j is a factor of num
            if num % j == 0:
                # Increment count of prime factors
                prime_factor_count += 1
                
                # Step 6: Remove all occurrences of the factor j from num
                while num % j == 0:
                    num //= j

        # Step 7: Check if the count of prime factors equals 2
        if prime_factor_count == 2:
            # Step 8: Increment the result counter for each valid i
            result_count += 1

    # Step 9: Output the result
    print(result_count)

# Call the function to execute the code
count_prime_numbers()
