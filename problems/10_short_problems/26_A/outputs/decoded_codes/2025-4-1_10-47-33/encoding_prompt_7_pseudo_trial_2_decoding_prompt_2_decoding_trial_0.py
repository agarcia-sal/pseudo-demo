def countSemiPrimes(t):
    totalSemiPrimes = 0
    
    for i in range(1, t + 1):
        divisorCount = 0
        currentNumber = i
        
        for j in range(2, i):
            if currentNumber % j == 0:
                divisorCount += 1
                while currentNumber % j == 0:
                    currentNumber //= j
        
        if divisorCount == 2:
            totalSemiPrimes += 1
    
    return totalSemiPrimes

# INPUT
t = int(input())

# OUTPUT
result = countSemiPrimes(t)
print(result)
