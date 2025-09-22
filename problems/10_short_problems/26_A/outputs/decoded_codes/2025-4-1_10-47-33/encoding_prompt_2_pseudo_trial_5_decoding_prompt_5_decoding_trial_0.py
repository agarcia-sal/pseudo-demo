# Function to count prime numbers up to a given number
def count_primes():
    # Step 1: Receive input for total numbers
    total_numbers = int(input())
    
    # Step 2: Initialize prime count variable
    prime_count = 0
    
    # Step 3: Loop through each number from 1 to totalNumbers
    for current_number in range(1, total_numbers + 1):
        # Initialize divisor count for the current number
        divisor_count = 0
        numerator = current_number
        
        # Step 4: Check for potential divisors starting from 2
        for potential_divisor in range(2, current_number):
            # Check if numerator is divisible by the potential divisor
            if numerator % potential_divisor == 0:
                divisor_count += 1  # Increment divisor count
                
                # Remove all factors of potential_divisor from numerator
                while numerator % potential_divisor == 0:
                    numerator //= potential_divisor
        
        # Step 5: Check if the divisor count indicates a prime number
        if divisor_count == 1:  # Only 1 divisor means the number is prime
            prime_count += 1
    
    # Output the total prime count found
    print(prime_count)

# Call the function to execute
count_primes()
