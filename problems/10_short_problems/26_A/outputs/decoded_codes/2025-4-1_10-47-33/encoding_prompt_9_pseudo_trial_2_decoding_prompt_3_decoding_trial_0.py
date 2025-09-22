def count_primes():
    # Step 1: Get User Input
    maximum_number = int(input())
    
    # Step 2: Initialize Count of Prime Numbers
    prime_count = 0

    # Step 3: Loop Through Each Number
    for current_number in range(2, maximum_number + 1):  # Start from 2 as 1 is not prime
        factor_count = 0
        remaining_number = current_number
        
        # Step 4: Check for Factors
        for potential_factor in range(2, current_number):  # Check factors up to current_number - 1
            if remaining_number % potential_factor == 0:
                factor_count += 1
                while remaining_number % potential_factor == 0:
                    remaining_number //= potential_factor  # This removes the factor
        
        # Step 5: Identify Prime Number
        if factor_count == 1:  # A prime has exactly one unique factor (itself)
            prime_count += 1

    # Step 6: Output the Result
    print(prime_count)

# Run the function to execute the code
count_primes()
