def count_primes():
    # Step 1: Receive input for the total number of integers to check for primality
    totalNumbers = int(input())
    
    # Step 2: Initialize primeCount to track the number of prime numbers
    primeCount = 0
    
    # Step 3: Loop through each number from 1 to totalNumbers (inclusive)
    for currentNumber in range(1, totalNumbers + 1):
        # Initialize divisorCount to count distinct divisors
        divisorCount = 0
        numerator = currentNumber
        
        # Step 4: Check potential divisors from 2 to currentNumber - 1
        for potentialDivisor in range(2, currentNumber):
            # Check if currentNumber is divisible by potentialDivisor
            if numerator % potentialDivisor == 0:
                # Increment divisorCount
                divisorCount += 1
                # Divide by potentialDivisor until no longer divisible
                while numerator % potentialDivisor == 0:
                    numerator //= potentialDivisor
        
        # Step 5: If the number has exactly 2 distinct divisors, it's prime
        if divisorCount == 1 and currentNumber > 1:  # Checking if there's one divisor (the potential divisor itself)
            primeCount += 1
    
    # Step 6: Output the total number of prime numbers found
    print(primeCount)

# Call the function to execute the prime counting
count_primes()
