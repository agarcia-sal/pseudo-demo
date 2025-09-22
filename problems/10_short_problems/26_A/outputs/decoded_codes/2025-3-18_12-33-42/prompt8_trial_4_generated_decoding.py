def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def semiprime_count(t):
    semiprimeCount = 0
    
    for currentNumber in range(1, t + 1):
        distinctPrimeCount = 0
        tempNumber = currentNumber
        
        for potentialFactor in range(2, currentNumber):
            if tempNumber % potentialFactor == 0:
                distinctPrimeCount += 1
                
                while tempNumber % potentialFactor == 0:
                    tempNumber //= potentialFactor
        
        if distinctPrimeCount == 2:
            semiprimeCount += 1
    
    return semiprimeCount

t = int(input())
result = semiprime_count(t)
print(result)
