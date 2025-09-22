# Accept an input integer 'upper_limit' representing the upper limit
upper_limit = int(input())

# Initialize a variable to track the count of prime numbers
prime_count = 0

# Loop through all integer values from 1 to upper_limit (inclusive)
for number in range(1, upper_limit + 1):
    # Initialize a counter for the number of unique prime factors
    unique_prime_factor_count = 0
    
    # Set the current number to evaluate for prime factors
    current_number = number

    # Check for prime factors starting from 2 up to (but not including) the current number
    for potential_prime_factor in range(2, current_number):
        # If the current number is divisible by the potential prime factor
        if current_number % potential_prime_factor == 0:
            # Increment the count of unique prime factors
            unique_prime_factor_count += 1
            
            # Divide current_number by potential_prime_factor until it's no longer divisible
            while current_number % potential_prime_factor == 0:
                current_number //= potential_prime_factor
            
    # If exactly two unique prime factors were found, it indicates the number is prime
    if unique_prime_factor_count == 2:
        # Increment the total count of prime numbers
        prime_count += 1

# Output the total count of prime numbers found
print(prime_count)
