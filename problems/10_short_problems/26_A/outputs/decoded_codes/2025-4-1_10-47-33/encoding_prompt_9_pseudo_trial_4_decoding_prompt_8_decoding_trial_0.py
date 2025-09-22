def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_products_of_two_distinct_primes(limit):
    countOfProducts = 0
    
    for currentNumber in range(1, limit + 1):
        distinctPrimeFactors = 0
        temporaryNumber = currentNumber

        for potentialPrime in range(2, currentNumber):
            if temporaryNumber % potentialPrime == 0 and is_prime(potentialPrime):
                distinctPrimeFactors += 1
                while temporaryNumber % potentialPrime == 0:
                    temporaryNumber //= potentialPrime
            
            if distinctPrimeFactors > 2:
                break
        
        if distinctPrimeFactors == 2:
            countOfProducts += 1

    return countOfProducts

limit = int(input())
result = count_products_of_two_distinct_primes(limit)
print(result)
