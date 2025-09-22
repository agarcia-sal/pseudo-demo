# Read a whole number from input that indicates the upper limit for checking numbers
upper_limit = int(input())  # Convert input to an integer

# Initialize a variable to count the number of semi-prime numbers found
semi_prime_count = 0

# Loop through all numbers from 1 to upper_limit, inclusive
for current_number in range(1, upper_limit + 1):
    # Initialize a counter for the number of prime factors found
    prime_factor_count = 0

    # Create a variable to work with the current number
    working_number = current_number

    # Check potential divisors starting from 2 up to just below current_number
    for divisor in range(2, current_number):
        # If the working_number is divisible by the current divisor
        if working_number % divisor == 0:
            # Increment the prime factor count
            prime_factor_count += 1
            
            # Continue dividing working_number by the divisor while it is divisible
            while working_number % divisor == 0:
                working_number //= divisor  # Use floor division to update working_number

    # If exactly two distinct prime factors were found, increment the semi-prime count
    if prime_factor_count == 2:
        semi_prime_count += 1

# Output the total count of semi-prime numbers found
print(semi_prime_count)
