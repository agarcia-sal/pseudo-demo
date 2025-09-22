def count_numbers_with_two_distinct_primes():
    t = int(input())
    result = 0

    for i in range(1, t + 1):
        countOfDistinctPrimes = 0
        currentNumber = i

        for j in range(2, i):  # Check for distinct prime factors
            if currentNumber % j == 0:
                countOfDistinctPrimes += 1
                
                # Factor out all occurrences of j
                while currentNumber % j == 0:
                    currentNumber //= j
            
            # If we already found two distinct primes, we can break
            if countOfDistinctPrimes > 2:
                break

        if countOfDistinctPrimes == 2:
            result += 1

    print(result)

# Example usage:
count_numbers_with_two_distinct_primes()
