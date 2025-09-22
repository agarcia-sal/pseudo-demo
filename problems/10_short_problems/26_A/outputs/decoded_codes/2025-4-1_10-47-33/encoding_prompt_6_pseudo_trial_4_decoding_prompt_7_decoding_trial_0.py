# Accept an input integer 'upperLimit' representing the upper limit
upperLimit = int(input())

# Initialize a variable to track the count of prime numbers
primeCount = 0

# Loop through all integer values from 1 to upperLimit (inclusive)
for number in range(1, upperLimit + 1):
    # Initialize a counter for the number of unique prime factors
    uniquePrimeFactorCount = 0
    
    # Set the current number to evaluate for prime factors
    currentNumber = number

    # Check for prime factors starting from 2 up to (but not including) the current number
    for potentialPrimeFactor in range(2, currentNumber):
        # If the current number is divisible by the potential prime factor
        if currentNumber % potentialPrimeFactor == 0:
            # Increment the count of unique prime factors
            uniquePrimeFactorCount += 1
            
            # Divide currentNumber by potentialPrimeFactor until it's no longer divisible
            while currentNumber % potentialPrimeFactor == 0:
                currentNumber //= potentialPrimeFactor
            
    # If exactly two unique prime factors were found, it indicates the number is prime
    if uniquePrimeFactorCount == 2:
        # Increment the total count of prime numbers
        primeCount += 1

# Output the total count of prime numbers found
print(primeCount)
