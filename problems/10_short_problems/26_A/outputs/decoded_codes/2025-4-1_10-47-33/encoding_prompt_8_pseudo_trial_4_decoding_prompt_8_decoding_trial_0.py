# Start Program

# Get Input
totalNumbers = int(input())

# Initialize Count
result = 0

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Iterate Through Numbers
for currentNumber in range(1, totalNumbers + 1):
    primeFactorCount = 0
    tempNumber = currentNumber
    
    # Check for Prime Factors
    for potentialFactor in range(2, currentNumber):
        if tempNumber % potentialFactor == 0 and is_prime(potentialFactor):
            primeFactorCount += 1
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor
    
    # Evaluate Condition
    if primeFactorCount == 2:
        result += 1

# Output the Result
print(result)

# End Program
