def count_semi_primes(limit):
    semi_prime_count = 0  # Counter for semi-primes
    
    for number in range(1, limit + 1):  # Loop through each number up to the limit
        divisor_count = 0  # Counter for divisors of the current number
        current_number = number
        
        # Check for divisors from 2 up to the current number
        for divisor in range(2, current_number):  # Loop through possible divisors
            if current_number % divisor == 0:  # Check if divisor is a factor
                divisor_count += 1  # Found a divisor
                # Divide out all occurrences of this divisor from current number
                while current_number % divisor == 0:  # While it can be divided
                    current_number //= divisor  # Reduce current number
                
        # A semi-prime has exactly two unique prime factors
        if divisor_count == 2:  # Check if we found exactly two prime factors
            semi_prime_count += 1  # Increase semi-prime count
    
    return semi_prime_count  # Output the count of semi-primes

# Main program execution
t = int(input())  # Read the limit from the user
print(count_semi_primes(t))  # Count semi-primes up to the input number and print the result
