# Function to count semi-prime numbers up to an integer t
def count_semi_primes():
    # Step 1: Initialize the total semi-primes counter
    totalSemiPrimes = 0

    # Step 2: Process each number from 1 to t inclusive
    t = int(input())
    for currentNumber in range(1, t + 1):
        divisorCount = 0
        tempNumber = currentNumber

        # Step 3: Find prime factors
        for potentialDivisor in range(2, currentNumber):
            if tempNumber % potentialDivisor == 0:  # Check divisibility
                divisorCount += 1

                # While tempNumber is divisible by potentialDivisor
                while tempNumber % potentialDivisor == 0:
                    tempNumber //= potentialDivisor  # Divide by potentialDivisor

        # Step 4: Check for semi-prime condition
        if divisorCount == 2:  # Exactly two distinct prime factors
            totalSemiPrimes += 1

    # Step 5: Output the result
    print(totalSemiPrimes)

# Call the function to execute the counting process
count_semi_primes()
