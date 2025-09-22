def count_primes():
    # Step 2: Read an integer input which represents the upper limit of the range
    total_numbers = int(input())

    # Step 3: Initialize prime counter
    prime_count = 0

    # Step 4: Iterate over each number from 1 to total_numbers
    for current_number in range(1, total_numbers + 1):
        divisor_count = 0  # Initialize the count of divisors for the current number
        
        # Step 5: Check for divisibility from 2 to current_number - 1
        for potential_divisor in range(2, current_number):
            if current_number % potential_divisor == 0:
                divisor_count += 1  # Found a divisor
                # Reduce tempNumber completely by its divisor
                while current_number % potential_divisor == 0:
                    current_number //= potential_divisor

        # Step 6: Determine if the current number is prime
        if divisor_count == 1:  # A prime number has exactly one divisor (itself)
            prime_count += 1  # Confirm current_number is prime
            
        if current_number == 1: 
            # Edge case handling: number 1 is not prime
            prime_count -= 1

    # Step 7: Output the result
    print(prime_count)

# Running the function to see the output
count_primes()
