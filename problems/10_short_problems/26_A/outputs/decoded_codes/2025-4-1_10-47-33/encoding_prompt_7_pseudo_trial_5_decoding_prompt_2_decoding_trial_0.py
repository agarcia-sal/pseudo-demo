def countSemiPrimes(inputNumber):
    resultCounter = 0  # Initialize result counter to 0
    
    for currentNumber in range(1, inputNumber + 1):  # Loop from 1 to inputNumber inclusive
        divisorCount = 0  # Initialize divisor count for the current number
        tempNumber = currentNumber  # Create a mutable copy of currentNumber
        
        for potentialDivisor in range(2, currentNumber):  # Loop through potential divisors
            if tempNumber % potentialDivisor == 0:  # If divisible
                divisorCount += 1  # Increment divisor count
                
                while tempNumber % potentialDivisor == 0:  # Factor out potentialDivisor
                    tempNumber //= potentialDivisor  # Divide tempNumber by potentialDivisor

        if divisorCount == 2:  # Check if exactly two distinct prime factors
            resultCounter += 1  # Increment result counter if semi-prime
    
    return resultCounter  # Return the count of semi-primes

# Example usage
t = int(input())  # Read user input as an integer
print(countSemiPrimes(t))  # Print the count of semi-primes up to t
