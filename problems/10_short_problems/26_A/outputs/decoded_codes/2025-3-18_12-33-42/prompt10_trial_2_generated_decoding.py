def count_numbers_with_two_distinct_prime_factors():
    # Input: Assume 't' is a positive integer input from the user
    t = int(input())  # Read input from user

    # Initialize the result counter to zero
    result_count = 0

    # Loop through each integer from 1 to t, inclusive
    for i in range(1, t + 1):
        distinct_prime_count = 0
        num = i  # Set num to the current integer i

        # Check for prime factors starting from 2 up to i
        for j in range(2, num + 1):
            # If j is a divisor of num
            if num % j == 0:  # Check if j divides num
                distinct_prime_count += 1  # Increment distinct prime factor count
                
                # Divide num by j until j is no longer a divisor
                while num % j == 0:
                    num //= j  # Reduce num by the prime factor j

            # Break early if we have already found 2 distinct prime factors
            if distinct_prime_count > 2:
                break

        # Check if the current number has exactly 2 distinct prime factors
        if distinct_prime_count == 2:
            result_count += 1  # Increment the result counter

    # Output the final count of numbers with exactly 2 distinct prime factors
    print(result_count)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
