t = int(input())
resultCount = 0

for currentNumber in range(1, t + 1):
    factorCount = 0
    currentValue = currentNumber
    
    for potentialFactor in range(2, currentNumber):
        if currentValue % potentialFactor == 0:
            factorCount += 1
            while currentValue % potentialFactor == 0:
                currentValue //= potentialFactor
                
    if factorCount == 2:
        resultCount += 1

print(resultCount)


def count_numbers_with_two_prime_factors(limit):
    count = 0
    
    for num in range(1, limit + 1):
        distinctPrimeFactors = 0
        currentValue = num
        
        for factor in range(2, int(num**0.5) + 1):
            if currentValue % factor == 0:
                distinctPrimeFactors += 1
                while currentValue % factor == 0:
                    currentValue //= factor
        
        if currentValue > 1:  # If there's a remaining prime factor > sqrt(num)
            distinctPrimeFactors += 1
        
        if distinctPrimeFactors == 2:
            count += 1
            
    return count

t = int(input())
result = count_numbers_with_two_prime_factors(t)
print(result)
