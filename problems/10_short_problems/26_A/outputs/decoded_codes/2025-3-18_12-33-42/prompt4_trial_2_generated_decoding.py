def count_numbers_with_two_unique_prime_factors():
    # Read an integer value from user input, representing the upper limit
    t = int(input())

    # Initialize a counter to track the number of numbers with exactly two unique prime factors
    prime_count = 0

    # Loop through all numbers from 1 to t
    for i in range(1, t + 1):
        # Reset the count of unique prime factors for the current number
        unique_prime_factor_count = 0
        current_number = i
        
        # Check for prime factors from 2 up to the current number
        for j in range(2, i):
            # If j is a factor of current_number, it is a prime factor
            if current_number % j == 0:
                unique_prime_factor_count += 1

                # Divide current_number by j until it is no longer divisible
                while current_number % j == 0:
                    current_number //= j
        
        # If the current number has exactly two unique prime factors, increment the count
        if unique_prime_factor_count == 2:
            prime_count += 1
            
    # Output the final count of numbers that have exactly two unique prime factors
    print(prime_count)

# Call the function to execute the logic
count_numbers_with_two_unique_prime_factors()
