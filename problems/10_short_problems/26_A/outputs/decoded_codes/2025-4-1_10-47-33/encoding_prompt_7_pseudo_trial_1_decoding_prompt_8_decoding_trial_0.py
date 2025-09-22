def countSemiPrimes(limit):
    semiPrimeCount = 0  # Counter for semi-primes
    
    for number in range(1, limit + 1):
        divisorCount = 0  # Counter for divisors of the current number
        currentNumber = number
        
        # Check for divisors from 2 up to current number - 1
        for divisor in range(2, currentNumber):
            if currentNumber % divisor == 0:  # Found a divisor
                divisorCount += 1  # Increment divisor count
                # Divide out all occurrences of this divisor from current number
                while currentNumber % divisor == 0:
                    currentNumber //= divisor  # Reduce current number
                
        # A semi-prime has exactly two unique prime factors
        if divisorCount == 2:
            semiPrimeCount += 1  # Increase semi-prime count
            
    return semiPrimeCount  # Output the count of semi-primes


# Main program execution
t = int(input())
result = countSemiPrimes(t)
print(result)
