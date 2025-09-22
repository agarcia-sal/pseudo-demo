# Initialize the total count of semi-prime numbers
total_semi_primes = 0

# Read the upper limit for checking semi-prime numbers
upper_limit = int(input())

# Process each number from 1 to upper_limit inclusive
for current_number in range(1, upper_limit + 1):
    divisor_count = 0  # Initialize the count of distinct prime factors
    temp_number = current_number  # Use a temporary variable to factorize

    # Find prime factors by checking potential divisors
    for potential_divisor in range(2, current_number):
        if temp_number % potential_divisor == 0:  # Check if divisible
            divisor_count += 1  # Increment count of prime factors
            
            # While the number is still divisible, divide it
            while temp_number % potential_divisor == 0:
                temp_number //= potential_divisor  # Use integer division

    # Check if the count of prime factors is exactly 2
    if divisor_count == 2:
        total_semi_primes += 1  # Increment the semi-prime total

# Output the final count of semi-prime numbers
print(total_semi_primes)
