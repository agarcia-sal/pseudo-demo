def count_prime_numbers():
    # Step 1: Receive an integer input called totalNumbers
    total_numbers = int(input())
    
    # Step 2: Initialize a variable primeCount to zero
    prime_count = 0
    
    # Step 3: Iterate through each number from 1 to totalNumbers (inclusive)
    for current_number in range(1, total_numbers + 1):
        # Initialize divisorCount for the current number
        divisor_count = 0
        numerator = current_number
        
        # Step 4: Check for potential divisors starting from 2
        for potential_divisor in range(2, current_number):
            # Check if numerator is divisible by potentialDivisor
            if numerator % potential_divisor == 0:
                # If it is, increment divisorCount
                divisor_count += 1
                
                # Remove all factors of potential_divisor from numerator
                while numerator % potential_divisor == 0:
                    numerator //= potential_divisor
        
        # Step 5: Check if divisorCount equals 2
        if divisor_count == 1 and current_number > 1:  # Prime numbers have exactly two distinct divisors: 1 and itself
            prime_count += 1
        
    # Step 6: Output the value of primeCount
    print(prime_count)

# Call the function to execute
count_prime_numbers()
