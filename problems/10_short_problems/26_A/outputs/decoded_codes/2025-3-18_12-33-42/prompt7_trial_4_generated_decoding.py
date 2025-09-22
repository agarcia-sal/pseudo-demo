def countDistinctPrimeNumbers(limit):
    # Initialize a counter for distinct prime numbers
    countOfDistinctPrimes = 0

    # Loop through each number from 1 to the specified limit
    for currentNumber in range(1, limit + 1):
        # Initialize a counter for the number of distinct prime factors
        primeFactorCount = 0
        number = currentNumber  # Use this variable to perform factorization

        # Loop to find potential prime factors
        for potentialFactor in range(2, currentNumber):
            # Check if the number is divisible by the potential factor
            if number % potentialFactor == 0:
                primeFactorCount += 1  # Increment the distinct prime factor count
                
                # Divide the number by the potential factor till it can't anymore
                while number % potentialFactor == 0:
                    number //= potentialFactor
        
        # Check if the count of distinct prime factors is exactly 2
        if primeFactorCount == 2:
            countOfDistinctPrimes += 1  # Increment the count for valid numbers

    # Output the total count of numbers with exactly two distinct prime factors
    print(countOfDistinctPrimes)

# Sample Usage: Uncomment the following lines to run the function
# limit_input = int(input())
# countDistinctPrimeNumbers(limit_input)
