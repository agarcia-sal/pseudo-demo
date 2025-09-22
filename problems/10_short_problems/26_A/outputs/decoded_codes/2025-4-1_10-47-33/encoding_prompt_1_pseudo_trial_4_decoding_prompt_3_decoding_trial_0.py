def count_numbers_with_two_distinct_prime_factors():
    # Read the upper limit from user input
    t = int(input())
    # Initialize result counter
    result = 0
    
    # Iterate through each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        count = 0  # To track distinct prime factors
        currentNumber = i  # The number we are currently factoring
        
        # Check for prime factors starting from 2 to one less than i
        for j in range(2, i):
            if currentNumber % j == 0:  # If j is a factor of currentNumber
                count += 1  # Found a new prime factor
                # Remove all occurrences of the prime factor j
                while currentNumber % j == 0:
                    currentNumber //= j
        
        # After checking all possible factors, if exactly two distinct primes are found
        if count == 2:
            result += 1  # Increment result
            
    # Output the result
    print(result)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
