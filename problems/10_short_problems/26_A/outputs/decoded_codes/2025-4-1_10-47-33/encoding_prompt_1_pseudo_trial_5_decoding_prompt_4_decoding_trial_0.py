def count_numbers_with_two_distinct_prime_factors():
    # Read the upper limit for checking numbers
    t = int(input())
    
    resultCount = 0  # To count numbers with exactly two distinct prime factors

    # Loop through each number from 1 to t
    for currentNumber in range(1, t + 1):
        distinctPrimeFactorsCount = 0  # Reset distinct prime factors count for the current number
        tempNumber = currentNumber  # Temporary variable to manipulate the current number

        # Check for prime factors starting from 2
        for potentialFactor in range(2, currentNumber):
            if tempNumber % potentialFactor == 0:  # If potentialFactor is a factor of tempNumber
                distinctPrimeFactorsCount += 1  # Found a distinct prime factor
                
                # Eliminate all occurrences of potentialFactor from tempNumber
                while tempNumber % potentialFactor == 0:
                    tempNumber //= potentialFactor

        # Check if the current number has exactly two distinct prime factors
        if distinctPrimeFactorsCount == 2:
            resultCount += 1  # Increment the result count

    # Output the final count of numbers with exactly two distinct prime factors
    print(resultCount)

# Call the function to execute
count_numbers_with_two_distinct_prime_factors()
