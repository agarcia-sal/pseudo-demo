# 1. Start Program

# 2. Get Input 
totalNumbers = int(input())

# 3. Initialize Result Counter
primeCount = 0  # this will store the count of prime numbers

# 4. Loop Through Each Number
for currentNumber in range(1, totalNumbers + 1):
    # 1. Set Divisor Count
    divisorCount = 0  # this will count how many divisors currentNumber has
    
    # 2. Set Working Number
    workingNumber = currentNumber

    # 3. Check for Divisibility
    for potentialDivisor in range(2, currentNumber):
        if workingNumber % potentialDivisor == 0:
            # 1. Increase Divisor Count
            divisorCount += 1
            # 2. Divide Until Not Divisible
            while workingNumber % potentialDivisor == 0:
                workingNumber //= potentialDivisor  # remove that prime factor
    
    # 4. Check If Number is Prime
    if divisorCount == 2:  # it has exactly two distinct positive divisors
        primeCount += 1

# 5. Output Result
print(primeCount)  # represents the total number of prime numbers found from 1 to totalNumbers
