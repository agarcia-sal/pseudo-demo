def countSemiprimes(limit):
    # Initializing the semiprime count
    semiprimeCount = 0
    
    # Loop through each number from 1 to the limit
    for i in range(1, limit + 1):
        # Counter for the number of distinct prime factors
        divisorCount = 0
        currentNumber = i
        
        # Check potential divisors from 2 to (i - 1)
        for potentialDivisor in range(2, i):
            # Check if the current number is divisible by the potential divisor
            if currentNumber % potentialDivisor == 0:
                # Increment the divisor count
                divisorCount += 1
                
                # Reduce current number by dividing until it's no longer divisible
                while currentNumber % potentialDivisor == 0:
                    currentNumber //= potentialDivisor
        
        # Check if exactly two distinct prime divisors were found
        if divisorCount == 2:
            semiprimeCount += 1
            
    # Return the total count of semiprimes found
    return semiprimeCount

# Read limit from user input
inputLimit = int(input())

# Call the function and store the output
output = countSemiprimes(inputLimit)

# Print the output
print(output)
