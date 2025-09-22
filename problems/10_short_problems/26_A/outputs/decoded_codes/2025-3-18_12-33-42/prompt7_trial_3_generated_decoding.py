def countSemiPrimes(limit):
    # Initialize the count of semi-primes
    semiPrimeCount = 0
    
    # Iterate over each number from 1 to limit
    for number in range(1, limit + 1):
        divisorCount = 0  # Reset divisor count for each number
        currentNumber = number  # Store the current number
        
        # Check potential divisors from 2 to (number - 1)
        for divisor in range(2, number):
            if currentNumber % divisor == 0:  # Check if divisible
                divisorCount += 1  # Found a divisor
                # Divide currentNumber by divisor until it's no longer divisible
                while currentNumber % divisor == 0:
                    currentNumber //= divisor
        
        # If exactly two distinct prime factors were found, it's a semi-prime
        if divisorCount == 2:
            semiPrimeCount += 1  # Increment the semi-prime count
            
    return semiPrimeCount  # Return the total count of semi-primes


# Main execution
t = int(input())  # Read input as an integer
result = countSemiPrimes(t)  # Call the function to count semi-primes
print(result)  # Print the result
