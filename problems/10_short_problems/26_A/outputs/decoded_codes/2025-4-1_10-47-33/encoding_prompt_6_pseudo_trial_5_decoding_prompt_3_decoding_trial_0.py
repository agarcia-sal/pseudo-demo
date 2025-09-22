def count_numbers_with_two_distinct_prime_factors():
    # Input: Read an integer `t` from the user
    t = int(input())
    
    # Initialize Result: Count of numbers with exactly two distinct prime factors
    totalCount = 0

    # Loop Through Each Number from 1 to `t`
    for currentNumber in range(1, t + 1):
        distinctPrimeCount = 0  # Track number of distinct prime factors
        currentValue = currentNumber
        
        # Find Prime Factors
        for potentialPrime in range(2, currentNumber):
            if currentValue % potentialPrime == 0:  # If potentialPrime is a factor
                distinctPrimeCount += 1  # Found a new distinct prime factor
                
                # Reduce currentValue to remove all instances of potentialPrime
                while currentValue % potentialPrime == 0:
                    currentValue //= potentialPrime
        
        # Check for Exactly Two Distinct Prime Factors
        if distinctPrimeCount == 2:
            totalCount += 1  # Increment count if there are exactly two distinct prime factors

    # Output the Result
    print(totalCount)

# Call the function
count_numbers_with_two_distinct_prime_factors()
