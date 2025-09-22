def count_numbers_with_two_prime_factors():
    # Read the input value indicating how many numbers to check
    total_numbers = int(input())
    
    # Initialize a counter for numbers with exactly two prime factors
    prime_factor_count = 0

    # Loop through each number from 1 to total_numbers
    for number in range(1, total_numbers + 1):
        # Initialize a count for prime factors found in the current number
        factor_count = 0
        current_number = number
        
        # Check for factors from 2 up to the current number (exclusive)
        for factor in range(2, current_number + 1):
            # If the factor divides the current number
            if current_number % factor == 0:
                # Increment the count of found prime factors
                factor_count += 1
                
                # Divide the current number by the factor until it no longer divides evenly
                while current_number % factor == 0:
                    current_number //= factor  # Use integer division for clarity
                    
            # If more than 2 distinct factors are found, we can break early
            if factor_count > 2:
                break
        
        # If exactly two distinct prime factors were found
        if factor_count == 2:
            # Increment the total count of such numbers
            prime_factor_count += 1

    # Output the total count of numbers with exactly two distinct prime factors
    print(prime_factor_count)

# Call the function to execute the logic
count_numbers_with_two_prime_factors()
