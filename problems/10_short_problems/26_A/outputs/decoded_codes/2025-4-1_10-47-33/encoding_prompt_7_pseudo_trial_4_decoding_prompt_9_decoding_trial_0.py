def countSemiPrimeNumbers(inputNumber):
    # Initialize result to count semi-prime numbers
    result = 0
    
    # Loop through each integer from 1 to inputNumber
    for currentInteger in range(1, inputNumber + 1):
        # Initialize count of prime factors
        prime_factor_count = 0
        currentNumber = currentInteger
        
        # Check for prime factors from 2 to currentInteger - 1
        for factor in range(2, currentInteger):
            # Check if currentNumber is divisible by the factor
            if currentNumber % factor == 0:
                # Found a prime factor, increment count
                prime_factor_count += 1
                
                # Factor out the prime factor completely
                while currentNumber % factor == 0:
                    currentNumber //= factor
            
        # Check if the count of prime factors is exactly 2
        if prime_factor_count == 2:
            # Increment the result as we found a semi-prime
            result += 1
            
    # Return the count of semi-prime numbers
    return result
