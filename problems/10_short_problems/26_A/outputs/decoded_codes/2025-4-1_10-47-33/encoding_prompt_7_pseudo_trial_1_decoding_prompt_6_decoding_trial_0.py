def count_semi_primes(limit):
    semi_prime_count = 0  # Counter for semi-primes

    # Loop through each number from 1 to limit
    for current_number in range(1, limit + 1):
        divisor_count = 0  # Counter for divisors of the current number
        temp_number = current_number  # Working variable to reduce the current number

        # Check for divisors from 2 up to current_number - 1
        for divisor in range(2, temp_number):
            if temp_number % divisor == 0:  # Check if divisible by the divisor
                divisor_count += 1  # Found a divisor
                
                # Divide out all occurrences of this divisor from temp_number
                while temp_number % divisor == 0:
                    temp_number //= divisor  # Reduce temp_number by divisor

        # A semi-prime has exactly two unique prime factors
        if divisor_count == 2:
            semi_prime_count += 1  # Increase semi-prime count
            
    return semi_prime_count  # Output the count of semi-primes

# Main program execution
t = int(input())  # Get user input as an integer
result = count_semi_primes(t)  # Count semi-primes up to the input number
print(result)  # Output the result
