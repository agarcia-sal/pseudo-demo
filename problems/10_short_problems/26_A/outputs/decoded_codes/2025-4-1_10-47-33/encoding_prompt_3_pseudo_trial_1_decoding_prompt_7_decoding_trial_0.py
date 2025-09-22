# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main function to count semi-prime numbers
def count_semi_primes():
    # Read the upper limit for semi-prime checking
    t = int(input())
    
    # Initialize counter for semi-prime numbers
    totalSemiPrimes = 0
    
    # Process each number from 1 to t inclusive
    for currentNumber in range(1, t + 1):
        divisorCount = 0
        tempNumber = currentNumber

        # Find prime factors
        # Iterate potential divisors from 2 to currentNumber - 1
        for potentialDivisor in range(2, currentNumber):
            if tempNumber % potentialDivisor == 0:
                divisorCount += 1  # Found a divisor
                # Divide tempNumber by potentialDivisor
                while tempNumber % potentialDivisor == 0:
                    tempNumber //= potentialDivisor
        
        # Check for semi-prime condition (exactly two distinct prime factors)
        if divisorCount == 2:
            totalSemiPrimes += 1  # Increment the count of semi-primes

    # Output the total number of semi-prime numbers found
    print(totalSemiPrimes)

# Call the function to execute
count_semi_primes()
