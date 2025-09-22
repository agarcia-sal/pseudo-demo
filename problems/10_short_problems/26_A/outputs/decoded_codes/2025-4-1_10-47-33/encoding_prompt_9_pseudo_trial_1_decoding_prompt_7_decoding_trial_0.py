# Program to count the number of prime numbers up to a specified integer

# Step 1: Get the Input
total = int(input())  # Read an integer value from the user

# Step 2: Initialize Count of Prime Numbers
primeCount = 0  # This will keep track of how many prime numbers are found

# Step 3: Iterate Through Possible Numbers
for currentNumber in range(1, total + 1):  # Loop from 1 to total inclusive
    # Initialize divisor count
    divisorCount = 0  # This will count how many divisors currentNumber has
    workingNum = currentNumber  # This number will be used for checking divisibility
    
    # Check for Divisibility
    for potentialDivisor in range(2, currentNumber):  # Loop for possible divisors
        if workingNum % potentialDivisor == 0:  # If workingNum is divisible by potentialDivisor
            divisorCount += 1  # Increment divisorCount
            # Divide workingNum by potentialDivisor until it is no longer divisible
            while workingNum % potentialDivisor == 0:
                workingNum //= potentialDivisor
    
    # Determine if currentNumber is Prime
    if divisorCount == 2:  # A prime number has exactly two divisors (1 and itself)
        primeCount += 1  # Increment primeCount if currentNumber is prime

# Step 4: Output Result
print(primeCount)  # Print the number of prime numbers found

# End Program
