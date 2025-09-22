def countSemiPrimes(inputNumber):
    # Initialize a counter for semi-prime numbers
    resultCounter = 0

    # Loop through each number from 1 to inputNumber
    for currentNumber in range(1, inputNumber + 1):
        divisorCount = 0  # Initialize a count for the number of distinct prime factors
        tempNumber = currentNumber  # Create a mutable copy of currentNumber for factorization

        # Check potential divisors from 2 to currentNumber - 1
        for potentialDivisor in range(2, currentNumber):
            # If tempNumber is divisible by potentialDivisor
            if tempNumber % potentialDivisor == 0:
                divisorCount += 1  # Increment the distinct divisor count
                
                # While tempNumber is divisible by potentialDivisor, divide it
                while tempNumber % potentialDivisor == 0:
                    tempNumber //= potentialDivisor  # Perform integer division

        # After checking all divisors, check if we found exactly two distinct prime factors
        if divisorCount == 2:
            resultCounter += 1  # Increment the result counter for semi-prime numbers

    # Return the total count of semi-prime numbers found
    return resultCounter

# Example usage
t = int(input())  # Read user input as an integer
print(countSemiPrimes(t))  # Print the number of semi-prime numbers up to t
