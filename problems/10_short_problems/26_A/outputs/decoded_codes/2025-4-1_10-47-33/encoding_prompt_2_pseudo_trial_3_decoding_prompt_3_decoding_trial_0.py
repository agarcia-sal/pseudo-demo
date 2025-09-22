def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Input the total count of numbers to check
    total_count = int(input())
    
    # Step 2: Initialize a result counter
    result = 0
    
    # Step 3: Loop through each number to analyze
    for current_number in range(1, total_count + 1):
        distinct_prime_count = 0  # Initialize distinct prime count
        temp_number = current_number  # Copy current number for factorization

        # Step 4: Find prime factors
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:  # Check divisibility
                distinct_prime_count += 1  # Found a new prime factor
                # Remove all occurrences of this prime factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
        
        # Step 5: Check if the count of distinct primes is exactly 2
        if distinct_prime_count == 2:
            result += 1  # Increment the result counter if condition is met
    
    # Step 6: Output the result
    print(result)

# Run the function
count_numbers_with_two_distinct_prime_factors()
