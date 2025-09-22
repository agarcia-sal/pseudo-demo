def count_numbers_with_two_prime_factors():
    # Step 1: Read integer input
    t = int(input())
    # Step 2: Initialize result
    result = 0

    # Step 3: Iterate through each number from 1 to t
    for i in range(1, t + 1):
        count = 0
        number = i
        
        # Step 4: Check for factors from 2 to i-1
        for j in range(2, i):
            if number % j == 0:  # Check if j is a factor of number
                count += 1  # Found a new distinct factor
                # Step 5: Divide number by j until it's no longer divisible
                while number % j == 0:
                    number //= j
        
        # Step 6: If count of distinct prime factors is 2, increment result
        if count == 2:
            result += 1

    # Output the final result
    print(result)

# Call the function to execute
count_numbers_with_two_prime_factors()
