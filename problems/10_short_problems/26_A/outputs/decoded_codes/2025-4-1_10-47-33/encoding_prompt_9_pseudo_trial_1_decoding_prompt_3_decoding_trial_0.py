def count_primes():
    # Step 2: Get the Input
    total = int(input())  # Read an integer value from the user
    
    # Step 3: Initialize Count of Prime Numbers
    prime_count = 0  # Counter for prime numbers found
    
    # Step 4: Iterate Through Possible Numbers
    for current_number in range(1, total + 1):
        divisor_count = 0  # Count of divisors for the current number
        
        # Skip 1, it is not prime
        if current_number == 1:
            continue
        
        # Step 4.2: Check for Divisibility
        for potential_divisor in range(2, current_number):
            if current_number % potential_divisor == 0:
                divisor_count += 1  # Increment divisor count
                # Divide current_number by potential_divisor until it's no longer divisible
                while current_number % potential_divisor == 0:
                    current_number //= potential_divisor
        
        # Step 4.4: Determine if Prime
        if divisor_count == 1:  # Only the number itself as a divisor
            prime_count += 1  # Increment prime count
    
    # Step 5: Output Result
    print(prime_count)  # Print the total number of prime numbers

# Execute the function
count_primes()
