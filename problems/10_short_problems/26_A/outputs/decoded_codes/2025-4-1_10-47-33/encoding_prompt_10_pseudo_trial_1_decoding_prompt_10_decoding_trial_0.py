def count_numbers_with_two_prime_factors():
    # Step 1: Declare and initialize variables
    test_cases = 0
    result_count = 0

    # Step 2: Input number of test cases
    test_cases = int(input())

    # Step 3: Loop through each number from 1 to test_cases
    for current_number in range(1, test_cases + 1):
        prime_factor_count = 0
        num = current_number
        
        # Step 4: Check for factors of the current number
        for potential_factor in range(2, current_number):
            if num % potential_factor == 0:  # If potential_factor is a factor of num
                prime_factor_count += 1
                
                # Step 5: Divide num by potential_factor as long as it's divisible
                while num % potential_factor == 0:
                    num //= potential_factor  # Reduce num by dividing by the factor
            
        # Step 6: Check if the number has exactly two prime factors
        if prime_factor_count == 2:
            result_count += 1  # Increment the count of numbers with exactly two prime factors
            
    # Step 7: Output the result
    print(result_count)

# Call the function to execute
count_numbers_with_two_prime_factors()
