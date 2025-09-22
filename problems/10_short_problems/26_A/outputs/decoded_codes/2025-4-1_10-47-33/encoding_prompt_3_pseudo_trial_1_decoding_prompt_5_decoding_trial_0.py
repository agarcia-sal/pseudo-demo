def count_semi_primes(upper_limit):
    # Initialize the count of semi-prime numbers
    total_semi_primes = 0

    # Process each number from 1 to upper_limit inclusive
    for current_number in range(1, upper_limit + 1):
        divisor_count = 0
        temp_number = current_number
        
        # Find prime factors
        for potential_divisor in range(2, current_number):
            # Check if potential_divisor is a factor of temp_number
            if temp_number % potential_divisor == 0:
                divisor_count += 1
                
                # Divide temp_number by potential_divisor until it's no longer divisible
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor
        
        # Check for semi-prime condition
        if divisor_count == 2:
            total_semi_primes += 1

    # Return the total count of semi-prime numbers
    return total_semi_primes

# Read input for upper limit
upper_limit = int(input())
# Call the function and print the result
print(count_semi_primes(upper_limit))
