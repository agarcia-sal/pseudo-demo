def count_numbers_with_two_distinct_prime_factors():
    # Read the upper limit 't' from user input
    t = int(input())
    
    # Initialize a variable to count the numbers with exactly two distinct prime factors
    result = 0

    # Iterate through each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        count = 0  # Reset count of distinct prime factors for the current number
        current_number = i  # Number to be factorized
        
        # Check for prime factors starting from 2 up to less than the current number
        for j in range(2, i):
            if current_number % j == 0:  # If j is a factor of current_number
                count += 1  # Found a new distinct prime factor
                
                # Remove all occurrences of the prime factor j from current_number
                while current_number % j == 0:
                    current_number //= j
                
            if count > 2:  # If more than two distinct prime factors found, break early
                break

        # After checking all possible factors, check if we found exactly two distinct prime factors
        if count == 2:
            result += 1  # Increment the result count

    # Output the result
    print(result)

# Call the function to execute the logic
count_numbers_with_two_distinct_prime_factors()
