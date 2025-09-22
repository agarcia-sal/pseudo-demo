def countSemiPrimes(input_number):
    # Initialize the result counter for semi-prime numbers
    result_counter = 0
    
    # Loop through each number from 1 to input_number
    for current_number in range(1, input_number + 1):
        # Initialize the divisor count for the current number
        divisor_count = 0
        # Create a mutable version of the current number for factorization
        temp_number = current_number
        
        # Check for potential divisors from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            # If temp_number is divisible by potential_divisor
            if temp_number % potential_divisor == 0:
                # Increment the divisor count
                divisor_count += 1
                
                # Divide temp_number by potential_divisor until it can't anymore
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
        
        # If exactly two distinct prime factors are found, it's a semi-prime
        if divisor_count == 2:
            result_counter += 1
            
    # Return the result counter which holds number of semi-prime numbers
    return result_counter

# Example usage
t = int(input())
print(countSemiPrimes(t))

# Test cases can be implemented to check edge cases
# Example: 
# countSemiPrimes(0) should return 0
# countSemiPrimes(1) should return 0
# countSemiPrimes(10) should return 4 (the semi-primes are 4, 6, 9, and 10)
