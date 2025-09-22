def count_numbers_with_two_distinct_prime_factors():
    # Read integer input as `t`
    t = int(input())
    
    # Initialize a variable `result` to count the numbers with exactly two distinct prime factors
    result = 0

    # Loop through each integer `i` from 1 to `t` (inclusive)
    for i in range(1, t + 1):
        count = 0  # Initialize a counter for distinct prime factors
        number = i  # Set number to the current value of `i`
        
        # Check for prime factors from 2 to `i-1`
        for j in range(2, i):
            if number % j == 0:  # Check if `j` is a factor of `number`
                count += 1 # Increment the count of distinct prime factors
                while number % j == 0:  # Divide `number` by `j` until it's no longer divisible
                    number //= j
        
        # If count is equal to 2, increment the result
        if count == 2:
            result += 1

    # Output the final result
    print(result)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
