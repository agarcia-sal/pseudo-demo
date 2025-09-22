def count_numbers_with_two_prime_factors():
    # Read the input value, which represents the upper limit
    upperLimit = int(input())
    
    # Initialize a counter for the number of numbers that have exactly two prime factors
    resultCount = 0

    # Loop through each number from 1 to upperLimit
    for currentNumber in range(1, upperLimit + 1):
        # Initialize a counter to track the number of distinct prime factors for the current number
        primeFactorCount = 0
        
        # Initialize a variable to keep the current number for factorization
        tempNumber = currentNumber
        
        # Check for factors starting from 2 up to (currentNumber - 1)
        for potentialFactor in range(2, currentNumber):
            # If potentialFactor is a divisor of tempNumber
            if tempNumber % potentialFactor == 0:
                # Increment the count of distinct prime factors
                primeFactorCount += 1
                
                # While tempNumber is divisible by potentialFactor
                while tempNumber % potentialFactor == 0:
                    # Divide tempNumber by potentialFactor
                    tempNumber //= potentialFactor
        
        # If the current number has exactly two distinct prime factors
        if primeFactorCount == 2:
            # Increment the result count
            resultCount += 1

    # Output the final count of numbers with exactly two distinct prime factors
    print(resultCount)

# Call the function to execute
count_numbers_with_two_prime_factors()
