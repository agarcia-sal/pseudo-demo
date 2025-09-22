# Start Program

# Receive Input
limit = int(input())  # Prompt the user to enter a positive integer limit

# Initialize Count
countOfProducts = 0  # This variable holds the count of numbers that are products of exactly two distinct primes

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Iterate Through Numbers
for currentNumber in range(1, limit + 1):  # Loop through each number from 1 to limit
    distinctPrimeFactors = 0  # Initialize the distinct prime factors count
    temporaryNumber = currentNumber  # Store the current number for factorization
    
    # Check for Prime Factors
    for potentialPrime in range(2, currentNumber):  # Check potential primes from 2 to currentNumber - 1
        if is_prime(potentialPrime) and temporaryNumber % potentialPrime == 0:  # Check if it's prime and a factor
            distinctPrimeFactors += 1  # Found a distinct prime factor
            # Divide out all occurrences of this prime factor
            while temporaryNumber % potentialPrime == 0:
                temporaryNumber //= potentialPrime  # Reduce the number by the factor

    # Check the Condition
    if distinctPrimeFactors == 2:  # Check if we found exactly two distinct prime factors
        countOfProducts += 1  # Increment the count of valid products

# Output Result
print(countOfProducts)  # Print the total count of products up to limit

# End Program
