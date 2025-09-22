def count_primes():
    # Step 1: Read integer input
    upper_limit = int(input())
    
    # Initialize the count of prime numbers
    prime_count = 0
    
    # Step 3: Loop through each number from 1 to upper_limit (inclusive)
    for i in range(1, upper_limit + 1):
        # Initialize the count of divisors
        divisor_count = 0
        current_number = i
        
        # Step 4: Check for divisors from 2 to current_number (exclusive)
        for j in range(2, current_number):
            if current_number % j == 0:
                divisor_count += 1
                
                # Remove all factors of j from current_number
                while current_number % j == 0:
                    current_number //= j
        
        # Step 5: Determine if the current number is prime
        if divisor_count == 1 and i > 1:  # Only numbers > 1 can be prime
            prime_count += 1
    
    # Step 6: Output the count of prime numbers
    print(prime_count)

# You can call the function to run your code
count_primes()
