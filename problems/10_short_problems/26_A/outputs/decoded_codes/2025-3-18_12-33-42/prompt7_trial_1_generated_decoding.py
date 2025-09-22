def countDistinctPrimeFactors(inputTime):
    # Initialize total count of numbers with exactly two distinct prime factors
    totalCount = 0
    
    # Loop over each number from 1 to inputTime
    for currentNumber in range(1, inputTime + 1):
        # Initialize the count of distinct prime factors for the current number
        primeFactorCount = 0
        currentValue = currentNumber
        
        # Check for prime factors starting from 2 up to currentNumber - 1
        for factor in range(2, currentNumber):
            # If factor is a divisor of currentValue
            if currentValue % factor == 0:
                # Increase the count of distinct prime factors
                primeFactorCount += 1
                
                # Divide currentValue by factor until it no longer divides evenly
                while currentValue % factor == 0:
                    currentValue //= factor
        
        # Check if the number has exactly two distinct prime factors
        if primeFactorCount == 2:
            totalCount += 1  # Increment total count
    
    # Output: Return the count of numbers with exactly two distinct prime factors
    return totalCount

# Main execution
t = int(input())
print(countDistinctPrimeFactors(t))
