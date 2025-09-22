# Read the input value indicating how many numbers to check
totalNumbers = int(input())

# Initialize a counter for numbers with exactly two prime factors
primeFactorCount = 0

# Loop through each number from 1 to totalNumbers
for number in range(1, totalNumbers + 1):
    
    # Initialize a count for prime factors found in the current number
    factorCount = 0
    currentNumber = number
    
    # Check for factors from 2 up to the current number (exclusive)
    for factor in range(2, currentNumber + 1):
        
        # If the factor divides the current number
        if currentNumber % factor == 0:
            
            # Increment the count of found prime factors
            factorCount += 1
            
            # Divide the current number by the factor until it no longer divides evenly
            while currentNumber % factor == 0:
                currentNumber //= factor
            
        # Exit the loop early if we have found 3 or more prime factors
        if factorCount > 2:
            break
            
    # If exactly two distinct prime factors were found
    if factorCount == 2:
        # Increment the total count of such numbers
        primeFactorCount += 1

# Output the total count of numbers with exactly two distinct prime factors
print(primeFactorCount)
