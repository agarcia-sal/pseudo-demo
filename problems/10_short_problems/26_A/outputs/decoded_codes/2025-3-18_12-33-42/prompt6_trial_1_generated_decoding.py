# Read an integer input representing the upper limit
upper_limit = int(input())

# Initialize a counter for prime numbers
prime_count = 0

# Loop through all numbers from 1 to upper_limit
for current_number in range(1, upper_limit + 1):
    # Initialize a counter for the number of prime factors
    prime_factor_count = 0
    
    # Copy current_number to another variable for factorization
    factor_candidate = current_number
    
    # Check for divisors starting from 2 up to current_number - 1
    for potential_factor in range(2, current_number):
        # If potential_factor is a divisor of factor_candidate
        if factor_candidate % potential_factor == 0:
            # Increment the count of prime factors
            prime_factor_count += 1
            
            # Divide factor_candidate by potential_factor until it is no longer divisible
            while factor_candidate % potential_factor == 0:
                factor_candidate //= potential_factor
                
    # Check if the number has exactly 2 prime factors
    if prime_factor_count == 2:
        # Increment the total prime count
        prime_count += 1
        
# Output the total count of numbers with exactly two prime factors
print(prime_count)
