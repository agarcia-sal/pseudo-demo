# Step 1: Start

# Step 2: Prompt the user to input a number and store it in variable totalCount
totalCount = int(input())

# Step 3: Initialize a variable semiprimeCount to 0 to keep track of semiprime numbers
semiprimeCount = 0

# Step 4: For each number currentNumber from 1 to totalCount (inclusive)
for currentNumber in range(1, totalCount + 1):
    
    # Step 4a: Initialize a variable primeFactorCount to 0 to count distinct prime factors
    primeFactorCount = 0
    
    # Step 4b: Set a variable remainingNumber to currentNumber
    remainingNumber = currentNumber

    # Step 4c: For each number potentialPrime from 2 to one less than currentNumber
    for potentialPrime in range(2, currentNumber):
        
        # Step 4ci: If remainingNumber is divisible by potentialPrime
        if remainingNumber % potentialPrime == 0:
            # Increment primeFactorCount by 1
            primeFactorCount += 1
            
            # Step 4cii: While remainingNumber is divisible by potentialPrime
            while remainingNumber % potentialPrime == 0:
                # Divide remainingNumber by potentialPrime to remove this factor
                remainingNumber //= potentialPrime

    # Step 4d: If primeFactorCount is equal to 2
    if primeFactorCount == 2:
        # Increment semiprimeCount by 1
        semiprimeCount += 1

# Step 5: After checking all numbers, output the value of semiprimeCount
print(semiprimeCount)

# Step 6: End
