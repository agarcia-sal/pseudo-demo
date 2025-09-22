def countSemiPrimeNumbers(inputNumber):
    # Initialize result to count semi-prime numbers
    result = 0
    
    # Iterate over each integer from 1 to inputNumber
    for currentInteger in range(1, inputNumber + 1):
        # Initialize count of prime factors to 0
        prime_factor_count = 0
        currentNumber = currentInteger  # Set currentNumber to the current integer
        
        # Check for prime factors by iterating from 2 to currentInteger - 1
        for i in range(2, currentInteger):
            if currentNumber % i == 0:  # If i is a factor of currentNumber
                prime_factor_count += 1  # Increment the count of prime factors
                
                # Divide currentNumber by i while it is divisible by i
                while currentNumber % i == 0:
                    currentNumber //= i  # Update currentNumber by dividing by the factor
            
            # Early exit if we already found more than 2 prime factors
            if prime_factor_count > 2:
                break
        
        # If the count of prime factors is exactly 2, it is a semi-prime
        if prime_factor_count == 2:
            result += 1
    
    # Return the count of semi-prime numbers
    return result

# Example code to call the function and print results for testing
inputNumber = int(input())  # Read an integer input
print(countSemiPrimeNumbers(inputNumber))  # Output the count of semi-prime numbers
