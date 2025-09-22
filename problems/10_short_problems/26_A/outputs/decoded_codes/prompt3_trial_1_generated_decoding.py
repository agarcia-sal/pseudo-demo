def count_primes():
    # Step 1: Initialize a variable to hold the count of prime numbers found.
    total = 0
    
    # Step 2: Read the integer input 't' which defines the range.
    t = int(input())
    
    # Step 3: Loop through each integer from 1 to 't'.
    for current_number in range(1, t + 1):
        # Step 3a: Initialize divisor count for the current number.
        divisor_count = 0
        
        # Step 3b: Set temp_number for factorization.
        temp_number = current_number
        
        # Step 3c: Check for potential factors.
        for potential_factor in range(2, current_number):
            # Step 3c.i: Check if temp_number is divisible by potential_factor.
            if temp_number % potential_factor == 0:
                # A new prime factor is found, increment the count.
                divisor_count += 1
                
                # Continuously divide temp_number by potential_factor.
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # Step 3d: Check if the number has exactly two distinct prime factors.
        if divisor_count == 2:
            total += 1  # Increment the total count of prime numbers.
    
    # After processing, output the total count of primes.
    print(total)

# To run the function
count_primes()
