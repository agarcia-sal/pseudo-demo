def count_primes():
    # Get input from the user
    t = int(input())
    
    # Initialize the counter for prime numbers
    prime_count = 0

    # Loop through each number from 1 to t (inclusive)
    for current_number in range(1, t + 1):
        divisor_count = 0  # Counter for divisors
        remaining_value = current_number  # Keep track of the number being checked

        # Check for potential divisors from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            # If remaining_value is divisible by potential_divisor
            if remaining_value % potential_divisor == 0:
                divisor_count += 1
                
                # Remove all occurrences of potential_divisor from remaining_value
                while remaining_value % potential_divisor == 0:
                    remaining_value //= potential_divisor

        # If the number has exactly 2 divisors, it's a prime number (1 and itself)
        if divisor_count == 1:
            prime_count += 1

    # Output the final count of prime numbers
    print(prime_count)

# Call the function to execute the prime counting
count_primes()
