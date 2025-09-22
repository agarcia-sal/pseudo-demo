def count_semi_primes(input_number):
    # Initialize the result counter to keep track of semi-primes found
    result_counter = 0
    
    # Loop through each number from 1 to input_number
    for current_number in range(1, input_number + 1):
        # Initialize divisor count for the current number
        divisor_count = 0
        temp_number = current_number  # Create a mutable copy for factorization
        
        # Loop through potential divisors from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            # Check if temp_number is divisible by potential_divisor
            if temp_number % potential_divisor == 0:
                divisor_count += 1  # Increment the divisor count
                
                # Continuously divide temp_number by potential_divisor
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor  # Integer division
                
        # Check if the number of unique prime factors is exactly 2
        if divisor_count == 2:
            result_counter += 1  # Increment semi-prime count
    
    return result_counter  # Return the count of semi-primes found

# Example usage
t = int(input())  # Read an integer input from the user
print(count_semi_primes(t))  # Call the function and print the result
