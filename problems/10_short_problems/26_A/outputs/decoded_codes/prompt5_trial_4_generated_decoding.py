# Function to count prime numbers up to a given limit
def count_primes():
    # Accept the limit for checking prime numbers from user input
    limit = int(input())  # User inputs the upper limit

    # Initialize a counter for prime numbers found
    prime_count = 0

    # Loop through each number from 2 to the limit
    for current_number in range(2, limit + 1):
        divisor_count = 0  # Counter for divisors of the current number
        
        # Check potential divisors from 2 up to current_number - 1
        for potential_divisor in range(2, current_number):
            # Check if the current number is divisible by the potential divisor
            if current_number % potential_divisor == 0:
                divisor_count += 1  # Found a divisor, increment the count
                
                # Keep dividing the current number by the potential divisor until it can no longer be divided
                while current_number % potential_divisor == 0:
                    current_number /= potential_divisor

        # A prime number must have exactly two divisors: 1 and itself
        if divisor_count == 1:  # Note: Adjusting count: Only needs one different divisor counted
            prime_count += 1  # Increment the prime number counter

    # Output the total count of prime numbers found
    print(prime_count)

# Function call to execute the prime counting
count_primes()
