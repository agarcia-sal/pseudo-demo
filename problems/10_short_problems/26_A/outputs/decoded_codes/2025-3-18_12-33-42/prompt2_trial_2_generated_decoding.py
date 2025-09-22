# Step 1: Request an integer input from the user
maxNumber = int(input())

# Step 2: Initialize variable to keep track of prime count
primeCount = 0

# Step 3: Loop through each number from 1 to maxNumber (inclusive)
for currentNumber in range(1, maxNumber + 1):
    # Set factorCount to zero for the current number
    factorCount = 0
    # For factorization purposes, set tempNumber to currentNumber
    tempNumber = currentNumber
    
    # Step 4: Check possible divisors from 2 up to but not including currentNumber
    for potentialFactor in range(2, currentNumber):
        if tempNumber % potentialFactor == 0:  # Check divisibility
            # If divisible, increment factorCount
            factorCount += 1
            
            # Sub-loop to completely divide tempNumber by potentialFactor
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor  # Remove the factor completely
    
    # Step 5: Check if factorCount is exactly 2
    if factorCount == 2:
        primeCount += 1  # Increment primeCount if currentNumber is prime

# Step 6: Display the value of primeCount
print(primeCount)
