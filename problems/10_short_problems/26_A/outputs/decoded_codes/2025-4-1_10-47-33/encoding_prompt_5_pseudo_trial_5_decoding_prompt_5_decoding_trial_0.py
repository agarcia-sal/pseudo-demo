# Function to count prime numbers up to a specified number
def count_primes():
    # Read the upper limit of the range
    total_numbers = int(input())
    
    # Initialize the prime count
    prime_count = 0
    
    # Iterate over each number in the specified range
    for current_number in range(1, total_numbers + 1):
        divisor_count = 0  # Count of divisors
        temp_number = current_number  # Temporary variable for division checks
        
        # Check for divisibility using potential divisors
        for potential_divisor in range(2, current_number):
            if temp_number % potential_divisor == 0:  # If divisible
                divisor_count += 1  # Count the divisor
                # Reduce temp_number by the current divisor
                while temp_number % potential_divisor == 0:
                    temp_number //= potential_divisor  # Factor out the divisor
        
        # Determine if current_number is prime
        if divisor_count == 1:  # Only divisible by 1 and itself
            prime_count += 1  # Increment prime number count
    
    # Output the total number of prime numbers found
    print(prime_count)

# Call the function to execute
count_primes()
