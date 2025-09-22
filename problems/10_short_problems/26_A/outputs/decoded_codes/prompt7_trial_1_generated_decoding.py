def countSemiPrimeNumbers(t):
    # Initialize the result variable to hold the total count of semi-prime numbers
    semiPrimeCount = 0

    # Iterate through each number from 1 to t (inclusive)
    for i in range(1, t + 1):
        # Initialize a counter for the number of prime factors found
        primeFactorCount = 0
        currentNumber = i

        # Check for potential prime factors starting from 2 up to currentNumber - 1
        for j in range(2, currentNumber):
            # If j is a divisor of currentNumber
            if currentNumber % j == 0:
                # Increment the prime factor count
                primeFactorCount += 1

                # Divide currentNumber by j until it no longer divides evenly
                while currentNumber % j == 0:
                    currentNumber //= j

        # Check if the number has exactly two distinct prime factors
        if primeFactorCount == 2:
            # Increment the semi-prime count
            semiPrimeCount += 1

    # Output the total count of semi-prime numbers found
    print(semiPrimeCount)

# Read an integer input for t
inputNumber = int(input())

# Call the function to count semi-prime numbers up to the input number
countSemiPrimeNumbers(inputNumber)
