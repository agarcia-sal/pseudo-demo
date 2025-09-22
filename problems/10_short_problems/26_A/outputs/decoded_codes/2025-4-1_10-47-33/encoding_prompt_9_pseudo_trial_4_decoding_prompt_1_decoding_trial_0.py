# Start Program

# Receive Input
limit = int(input())

# Initialize Count
countOfProducts = 0 

# Iterate Through Numbers
for currentNumber in range(1, limit + 1):
    distinctPrimeFactors = 0  # Initialize distinct prime factors count
    temporaryNumber = currentNumber  # Set temporary number
    
    # Check for Prime Factors
    for potentialPrime in range(2, currentNumber):
        if temporaryNumber % potentialPrime == 0:  # Check if divisible
            distinctPrimeFactors += 1  # Increment distinct prime factors
            while temporaryNumber % potentialPrime == 0:  # Remove that factor
                temporaryNumber //= potentialPrime  

    # Check the Condition
    if distinctPrimeFactors == 2:  
        countOfProducts += 1  # Increment product count

# Output Result
print(countOfProducts)  # Print count of products

# End Program
