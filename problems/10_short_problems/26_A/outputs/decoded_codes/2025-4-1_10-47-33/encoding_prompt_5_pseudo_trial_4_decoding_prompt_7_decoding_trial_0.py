# Function to count semiprime numbers up to a specified limit
def count_semiprimes():
    # Read input for the upper limit
    limit = int(input())
    
    # Initialize the semiprime count
    semiprimeCount = 0

    # Loop through each number from 1 to limit
    for currentNumber in range(1, limit + 1):
        # Count distinct prime factors of currentNumber
        primeFactorCount = 0
        numberToCheck = currentNumber
        
        # Check for potential prime factors
        for potentialPrime in range(2, currentNumber):
            # If potentialPrime is a factor of numberToCheck
            if numberToCheck % potentialPrime == 0:
                primeFactorCount += 1  # Found a prime factor
                
                # Divide out all instances of potentialPrime
                while numberToCheck % potentialPrime == 0:
                    numberToCheck //= potentialPrime
        
        # If exactly two distinct prime factors were found, increment semiprime count
        if primeFactorCount == 2:
            semiprimeCount += 1
    
    # Output the total count of semiprime numbers
    print(semiprimeCount)

# Call the function to execute
count_semiprimes()
