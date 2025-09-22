def count_numbers_with_two_prime_factors():
    # Read an integer input 'timePeriod'
    time_period = int(input())
    # Initialize 'resultCount' to 0
    result_count = 0

    # For each integer 'currentNumber' from 1 to 'timePeriod' (inclusive)
    for current_number in range(1, time_period + 1):
        # Initialize 'divisorCount' to 0
        divisor_count = 0
        # Set 'tempNumber' to 'currentNumber'
        temp_number = current_number
        
        # Check for potential divisors from 2 to 'currentNumber' - 1
        for potential_divisor in range(2, current_number):
            # If 'tempNumber' is divisible by 'potentialDivisor'
            if temp_number % potential_divisor == 0:
                # Increment 'divisorCount' by 1
                divisor_count += 1
                # While 'tempNumber' is divisible by 'potentialDivisor'
                while temp_number % potential_divisor == 0:
                    # Divide 'tempNumber' by 'potentialDivisor'
                    temp_number //= potential_divisor
        
        # If 'divisorCount' equals 2
        if divisor_count == 2:
            # Increment 'resultCount' by 1
            result_count += 1
    
    # Print 'resultCount'
    print(result_count)

# Run the function
count_numbers_with_two_prime_factors()
