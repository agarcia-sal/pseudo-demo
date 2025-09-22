# Function to count prime numbers up to a specified upper limit
def count_primes():
    # Step 1: Get the upper limit for prime number search from the user
    upper_limit = int(input())  # Read upper limit
    
    # Step 2: Initialize a variable to keep track of the count of prime numbers
    prime_count = 0

    # Step 3: Loop through all numbers from 1 to the upper limit
    for number in range(1, upper_limit + 1):
        # Step 4: Initialize a counter for prime factors
        factor_count = 0
        
        # Step 5: Set a temporary variable to check divisibility
        current_num = number

        # Step 6: Check for factors from 2 up to (but not including) the current number
        for potential_factor in range(2, number):
            # Step 7: If the current number is divisible by the potential factor
            if current_num % potential_factor == 0:
                # Increase the count of factors found
                factor_count += 1
                
                # Keep dividing the current number by the potential factor 
                # until it is no longer divisible
                while current_num % potential_factor == 0:
                    current_num //= potential_factor
        
        # Step 8: Check if the number has exactly 2 factors (indicating it is prime)
        if factor_count == 1:
            # Step 9: If it is prime, increment the prime count
            prime_count += 1

    # Step 10: Output the total count of prime numbers
    print("Total prime numbers between 1 and", upper_limit, "is:", prime_count)

# Example of how the function might be called
count_primes()
