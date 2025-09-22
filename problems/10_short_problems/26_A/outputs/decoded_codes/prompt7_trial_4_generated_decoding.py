def countDistinctPrimeNumbers(maxNumber):
    # This will store the total count of distinct prime numbers
    resultCount = 0  
    
    # Iterate over each number from 1 to maxNumber
    for currentNumber in range(1, maxNumber + 1):
        # Counter for distinct prime factors
        distinctPrimeCount = 0  
        divisibleNumber = currentNumber  # Store the current number for factorization

        # Check for prime factors starting from 2
        for potentialPrime in range(2, currentNumber):
            # If potentialPrime divides divisibleNumber
            if divisibleNumber % potentialPrime == 0:
                distinctPrimeCount += 1  # Found a new distinct prime factor

                # Divide out all occurrences of potentialPrime from divisibleNumber
                while divisibleNumber % potentialPrime == 0:
                    divisibleNumber //= potentialPrime  # Reduce the number
            # If we already found 2 distinct primes, no need to continue
            if distinctPrimeCount > 2:
                break 

        # If exactly two distinct prime factors were found, count this number
        if distinctPrimeCount == 2:
            resultCount += 1  # Increment result count for a valid number
    
    return resultCount  # Return the total count of numbers with two distinct prime factors

# Main execution starts here
maxNumber = int(input())  # Read the input value for the maximum number
result = countDistinctPrimeNumbers(maxNumber)  # Execute the function with the input value
print(result)  # Print the result of the count
