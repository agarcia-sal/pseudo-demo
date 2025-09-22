# Step 1: Receive an integer input which represents the upper limit (t).
upperLimit = int(input())

# Step 2: Initialize a variable to store the count of semiprime numbers.
semiprimeCount = 0

# Step 3: Loop from 1 through upperLimit (inclusive):
for currentNumber in range(1, upperLimit + 1):

    # Step 3.1: Initialize a variable to count the distinct prime factors for the current number.
    distinctPrimeFactorCount = 0
    numberToCheck = currentNumber

    # Step 3.2: Loop through all potential factors from 2 to currentNumber - 1:
    for potentialFactor in range(2, currentNumber):
        
        # Step 3.2.1: Check if potentialFactor is a factor of numberToCheck:
        if numberToCheck % potentialFactor == 0:

            # Increment the count of distinct prime factors.
            distinctPrimeFactorCount += 1
            
            # Divide numberToCheck by potentialFactor repeatedly until it's no longer divisible.
            while numberToCheck % potentialFactor == 0:
                numberToCheck //= potentialFactor

    # Step 3.3: After checking all potential factors, see if there are exactly 2 distinct prime factors:
    if distinctPrimeFactorCount == 2:
        # If yes, increment the semiprime count.
        semiprimeCount += 1

# Step 4: After the loop ends, display the count of semiprime numbers.
print(semiprimeCount)
