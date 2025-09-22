def countSemiPrimeNumbers():
    inputNumber = int(input())
    result = 0
    
    for currentInteger in range(2, inputNumber + 1):  # Start from 2 since 1 is not a semi-prime
        prime_factor_count = 0
        currentNumber = currentInteger
        
        for i in range(2, currentInteger):  # Check for factors starting from 2
            if currentNumber % i == 0:  # i is a prime factor
                prime_factor_count += 1
                while currentNumber % i == 0:  # Remove all occurrences of the prime factor
                    currentNumber //= i
            if prime_factor_count > 2:  # Early exit if more than 2 prime factors
                break
        
        if prime_factor_count == 2:  # Check if exactly two distinct prime factors
            result += 1
            
    return result
