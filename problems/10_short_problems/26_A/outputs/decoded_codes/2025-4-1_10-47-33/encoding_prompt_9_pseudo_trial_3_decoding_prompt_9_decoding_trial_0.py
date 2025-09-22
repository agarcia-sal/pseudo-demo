# Start the program and read an integer t from the user, representing the upper limit
t = int(input())

# Initialize a count variable named semiprimeCount to 0
semiprimeCount = 0

# Loop through each number currentNumber from 1 to t (inclusive)
for currentNumber in range(1, t + 1):
    # Set a counter named distinctPrimeCount to 0
    distinctPrimeCount = 0
    # Set a variable number equal to currentNumber
    number = currentNumber
    
    # Loop through each potential factor starting from 2 up to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        # Check if the current number is divisible by potentialFactor
        if number % potentialFactor == 0:
            # Increase distinctPrimeCount by 1
            distinctPrimeCount += 1
            # While the current number is divisible by potentialFactor
            while number % potentialFactor == 0:
                # Divide number by potentialFactor
                number //= potentialFactor
            
    # After checking all potential factors
    # If distinctPrimeCount is equal to 2
    if distinctPrimeCount == 2:
        # Increase semiprimeCount by 1
        semiprimeCount += 1

# Once all numbers have been checked, output the value of semiprimeCount
print(semiprimeCount)
