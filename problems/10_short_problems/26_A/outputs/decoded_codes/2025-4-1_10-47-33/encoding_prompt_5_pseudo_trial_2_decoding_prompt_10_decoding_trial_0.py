def count_primes():
    # Step 1: Get input from the user
    t = int(input())
    
    # Step 2: Initialize the prime count
    prime_count = 0
    
    # Step 3: Loop through each number from 1 to t
    for current_number in range(1, t + 1):
        divisor_count = 0
        remaining_value = current_number
        
        # Step 4: Check for divisibility with potential divisors
        for potential_divisor in range(2, current_number):
            if remaining_value % potential_divisor == 0:
                divisor_count += 1
                # Remove all occurrences of potential_divisor from remaining_value
                while remaining_value % potential_divisor == 0:
                    remaining_value //= potential_divisor
        
        # Step 5: Determine if the current number is prime
        if divisor_count == 2:
            prime_count += 1
            
    # Step 6: Output the result
    print(prime_count)

# Call the function to execute
count_primes()
