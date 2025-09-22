# 1. Start Program

# 2. Get the Input:
total = int(input())  # Read an integer value for upper limit

# 3. Initialize Count of Prime Numbers:
primeCount = 0  # Initialize prime count

# 4. Iterate Through Possible Numbers:
for currentNumber in range(1, total + 1):  # Loop through numbers from 1 to total
    divisorCount = 0  # Initialize divisor count
    workingNum = currentNumber  # Assign current number to working number
    
    # 3. Check for Divisibility:
    for potentialDivisor in range(2, workingNum):  # Check divisibility from 2 to currentNumber - 1
        if workingNum % potentialDivisor == 0:  # Check if divisible
            divisorCount += 1  # Increment divisor count
            while workingNum % potentialDivisor == 0:  # Reduce workingNum
                workingNum //= potentialDivisor  # Divide working number by potential divisor

    # 4. Determine if Prime:
    if divisorCount == 2:  # If there are exactly 2 divisors (1 and itself)
        primeCount += 1  # Increment prime count

# 5. Output Result:
print(primeCount)  # Print the count of prime numbers

# 6. End Program
