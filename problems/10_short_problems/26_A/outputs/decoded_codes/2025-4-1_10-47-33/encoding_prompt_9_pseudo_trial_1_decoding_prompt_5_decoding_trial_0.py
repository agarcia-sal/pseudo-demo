# Function to count prime numbers up to a specified integer
def count_primes_up_to_total():
    # Step 2: Get the Input
    total = int(input())  # Read an integer value for the upper limit

    # Step 3: Initialize Count of Prime Numbers
    prime_count = 0  # Variable to count the number of primes found

    # Step 4: Iterate Through Possible Numbers
    for current_number in range(1, total + 1):
        divisor_count = 0  # Count of divisors for the current number
        working_num = current_number  # Number to check for prime status

        # Check for Divisibility
        for potential_divisor in range(2, current_number):
            if working_num % potential_divisor == 0:  # Check if divisible
                divisor_count += 1  # Increment divisor count
                # Divide working_num by potential_divisor until it is no longer divisible
                while working_num % potential_divisor == 0:
                    working_num //= potential_divisor

        # Step 4.4: Determine if Prime
        if divisor_count == 2:  # Only 2 divisors means it is prime
            prime_count += 1  # Increment prime count

    # Step 5: Output Result
    print(prime_count)  # Print the count of prime numbers

# Invoke the function
count_primes_up_to_total()
