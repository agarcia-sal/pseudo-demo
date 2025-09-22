def countSemiPrimeNumbers(inputNumber):
    result = 0
    for currentInteger in range(1, inputNumber + 1):
        prime_factor_count = 0
        currentNumber = currentInteger
        
        for integer in range(2, currentInteger):
            if currentNumber % integer == 0:
                prime_factor_count += 1
                while currentNumber % integer == 0:
                    currentNumber //= integer

        if prime_factor_count == 2:
            result += 1

    return result
