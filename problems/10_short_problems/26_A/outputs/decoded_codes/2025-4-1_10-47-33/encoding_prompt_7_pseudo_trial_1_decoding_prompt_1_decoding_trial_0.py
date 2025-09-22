def countSemiPrimes(limit):
    semiPrimeCount = 0  # Counter for semi-primes

    for number in range(1, limit + 1):  # Loop from 1 to limit
        divisorCount = 0  # Counter for divisors of the current number
        currentNumber = number
        
        # Check for divisors from 2 up to the current number - 1
        for divisor in range(2, currentNumber):  # Loop from 2 to currentNumber - 1
            if currentNumber % divisor == 0:  # Check if divisible
                divisorCount += 1  # Found a divisor
                
                # Divide out all occurrences of this divisor from current number
                while currentNumber % divisor == 0:  # While currentNumber is divisible by divisor
                    currentNumber = currentNumber // divisor  # Reduce current number
                
        # A semi-prime has exactly two unique prime factors
        if divisorCount == 2:  # Check if divisorCount is equal to 2
            semiPrimeCount += 1  # Increase semi-prime count

    return semiPrimeCount  # Output the count of semi-primes

# Main program execution
t = int(input())  # Get an integer input from the user
result = countSemiPrimes(t)  # Count semi-primes up to the input number
print(result)  # Print the result
