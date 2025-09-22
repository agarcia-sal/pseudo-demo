def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_numbers_with_two_distinct_primes():
    inputNumber = int(input())
    countOfNumbers = 0
    
    for currentNumber in range(2, inputNumber + 1):
        distinctPrimeCount = 0
        workingNumber = currentNumber
        
        for potentialFactor in range(2, currentNumber):
            if workingNumber % potentialFactor == 0 and is_prime(potentialFactor):
                distinctPrimeCount += 1
                
                while workingNumber % potentialFactor == 0:
                    workingNumber //= potentialFactor
                
            if distinctPrimeCount > 2:  # Exit early if we exceed the needed count
                break
                
        if distinctPrimeCount == 2:
            countOfNumbers += 1
            
    print(countOfNumbers)

count_numbers_with_two_distinct_primes()
