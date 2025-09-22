def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Input the upper limit for checking numbers
    t = int(input())
    
    # Step 2: Initialize the result count
    result = 0

    # Step 3: Loop through numbers from 1 to t (inclusive)
    for current_number in range(1, t + 1):
        # Initialize the count of distinct prime factors
        factor_count = 0
        temp_number = current_number
        
        # Step 4: Check for factors starting from 2
        for potential_factor in range(2, current_number):
            # Check if potential_factor is a factor of temp_number
            if temp_number % potential_factor == 0:
                # Found a distinct prime factor
                factor_count += 1
                
                # Remove all occurrences of the potential_factor from temp_number
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor
            
            # Break early if we already found 2 distinct factors
            if factor_count > 2:
                break
        
        # Step 5: If there are exactly two distinct prime factors
        if factor_count == 2:
            result += 1

    # Step 6: Output the result
    print(result)

# You can call the function to run the program
count_numbers_with_two_distinct_prime_factors()
