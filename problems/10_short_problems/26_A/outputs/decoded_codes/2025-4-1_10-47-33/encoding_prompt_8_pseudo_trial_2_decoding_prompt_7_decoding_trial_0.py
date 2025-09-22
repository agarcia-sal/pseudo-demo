# Function to count semiprime numbers up to a given limit
def count_semiprimes():
    # Step 1: Read an integer value called 'limit' from user input
    limit = int(input())
    
    # Step 2: Initialize a variable 'semiprimeCount' to 0
    semiprimeCount = 0
    
    # Step 3: For each integer 'currentNumber' from 1 to 'limit' (inclusive)
    for currentNumber in range(1, limit + 1):
        # Step 3a: Initialize 'primeFactorCount' to 0
        primeFactorCount = 0
        
        # Step 3b: Set 'tempNumber' to 'currentNumber'
        tempNumber = currentNumber
        
        # Step 3c: For each 'potentialFactor' from 2 to 'currentNumber' (exclusive)
        for potentialFactor in range(2, currentNumber):
            # Step 3c.i: Check if 'tempNumber' is divisible by 'potentialFactor'
            if tempNumber % potentialFactor == 0:
                # Step 3c.i: Increment 'primeFactorCount'
                primeFactorCount += 1
                
                # Step 3c.ii: While 'tempNumber' is divisible by 'potentialFactor'
                while tempNumber % potentialFactor == 0:
                    # Step 3c.ii: Divide 'tempNumber' by 'potentialFactor'
                    tempNumber //= potentialFactor
        
        # Step 3d: Check if 'primeFactorCount' is exactly 2
        if primeFactorCount == 2:
            # Increment 'semiprimeCount' (currentNumber is a semiprime)
            semiprimeCount += 1
    
    # Step 4: Output the value of 'semiprimeCount'
    print(semiprimeCount)

# Call the function to start the counting process
count_semiprimes()
