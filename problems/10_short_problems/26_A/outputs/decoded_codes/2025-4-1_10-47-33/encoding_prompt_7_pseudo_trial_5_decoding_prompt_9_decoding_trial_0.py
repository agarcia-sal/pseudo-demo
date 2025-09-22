def countSemiPrimes(inputNumber):
    # Initialize a counter for semi-prime numbers
    resultCounter = 0
    
    # Iterate through each number from 1 to inputNumber
    for currentNumber in range(1, inputNumber + 1):
        # Initialize a count of divisors for currentNumber
        divisorCount = 0
        tempNumber = currentNumber
        
        # Check for potential divisors from 2 to currentNumber - 1
        for potentialDivisor in range(2, currentNumber):
            if tempNumber % potentialDivisor == 0:  # Check if divisible
                divisorCount += 1  # Increment divisor count
                
                # Divide tempNumber by potentialDivisor while it's divisible
                while tempNumber % potentialDivisor == 0:
                    tempNumber //= potentialDivisor  # Integer division
                
        # If exactly two distinct prime factors were found, it's a semi-prime
        if divisorCount == 2:
            resultCounter += 1  # Increment the semi-prime counter

    return resultCounter  # Return the total count of semi-primes

# Example usage
t = int(input())  # Get user input as an integer
print(countSemiPrimes(t))  # Print the number of semi-prime numbers
