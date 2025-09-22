# 1. Start
# 2. Input the total number of integers, t.
t = int(input())

# 3. Initialize a counter for the result, resultCount, to 0.
resultCount = 0

# 4. For each integer from 1 to t, do the following:
for i in range(1, t + 1):
    # Set a counter, primeFactorCount, to 0.
    primeFactorCount = 0
    # Assign the current integer to a variable, currentNumber.
    currentNumber = i
    
    # 5. For each integer divisor starting from 2 up to currentNumber - 1, do the following:
    for divisor in range(2, currentNumber):
        # 6. Check if currentNumber is divisible by divisor:
        if currentNumber % divisor == 0:
            # If true, increase the primeFactorCount by 1.
            primeFactorCount += 1
            # 6. While currentNumber is still divisible by divisor, do the following:
            while currentNumber % divisor == 0:
                # Divide currentNumber by divisor.
                currentNumber //= divisor
    
    # 7. If primeFactorCount equals 2, then:
    if primeFactorCount == 2:
        # Increase the resultCount by 1.
        resultCount += 1

# 8. Output the value of resultCount.
print(resultCount)
# 9. End
