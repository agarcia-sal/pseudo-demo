def count_semi_primes(limit):
    # Counter for semi-primes
    semi_prime_count = 0
    
    # Iterate through each number from 1 to limit
    for number in range(1, limit + 1):
        # Counter for unique prime factors
        divisor_count = 0  
        current_number = number
        
        # Check for divisors from 2 up to current number - 1
        for divisor in range(2, current_number):
            # Check if the current_number is divisible by divisor
            if current_number % divisor == 0:
                divisor_count += 1  # Found a divisor
                
                # Divide out all occurrences of this divisor from current number
                while current_number % divisor == 0:
                    current_number //= divisor  # Reduce current number
        
        # A semi-prime has exactly two unique prime factors
        if divisor_count == 2:
            semi_prime_count += 1  # Increase semi-prime count
            
    return semi_prime_count  # Output the count of semi-primes

# Main program execution
t = int(input())  # Read integer input from the user
print(count_semi_primes(t))  # Count semi-primes up to the input number
