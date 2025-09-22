def countSemiPrimes(input_number):
    # Initialize a counter for semi-prime numbers
    result_counter = 0
    
    # Loop through each number from 1 to input_number
    for current_number in range(1, input_number + 1):
        divisor_count = 0  # Count of distinct prime factors
        temp_number = current_number  # To factorize the current_number
        
        # Check for potential divisors from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0:  # Check if divisible
                divisor_count += 1
                
                # Divide out all instances of this divisor
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
                
            # Early exit if we already found 2 distinct divisors
            if divisor_count > 2:
                break
        
        # If exactly two distinct prime factors, it's a semi-prime
        if divisor_count == 2:
            result_counter += 1
    
    return result_counter

# Example usage
t = int(input())  # Read the integer from user input
print(countSemiPrimes(t))  # Call the function and print the result
