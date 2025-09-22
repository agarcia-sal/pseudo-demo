def countSemiPrimes(limit):
    # Initialize semi-prime counter
    semiPrimeCount = 0  
    
    # Iterate through each number from 1 to limit
    for number in range(1, limit + 1):
        # Counter for unique prime factors
        divisorCount = 0  
        currentNumber = number  # Store the current number
        
        # Check for prime factors starting from 2 up to current number - 1
        for divisor in range(2, currentNumber):  
            if currentNumber % divisor == 0:  # If the divisor divides the number
                divisorCount += 1  # Found a divisor
                
                # Divide out all occurrences of this divisor from current number
                while currentNumber % divisor == 0:  
                    currentNumber = currentNumber // divisor  # Reduce current number
                # Once we find a unique prime factor, continue to next divisor to find more
            # If we already found 2 unique prime factors, no need to check further
            if divisorCount > 2:  
                break
        
        # A semi-prime has exactly two unique prime factors
        if divisorCount == 2:  
            semiPrimeCount += 1  # Increment the semi-prime count
            
    return semiPrimeCount  # Return the total count of semi-primes

# Main program execution
t = int(input())  # Get limit input from the user
print(countSemiPrimes(t))  # Output the count of semi-primes up to the input number
