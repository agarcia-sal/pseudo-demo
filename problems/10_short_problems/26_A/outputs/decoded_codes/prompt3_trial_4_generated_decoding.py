def count_numbers_with_two_prime_factors():
    # Step 1: Read the total number of test cases
    total_test_cases = int(input())
    
    # Step 2: Initialize a variable to keep track of the count of numbers with exactly two prime factors
    prime_factor_count = 0

    # Step 3: Iterate through each number from 1 to total_test_cases
    for current_number in range(1, total_test_cases + 1):
        # Step 4: Initialize a counter for prime factors
        prime_factor_counter = 0
        original_number = current_number  # Store the original number for later use

        # Step 5: Check for factors starting from 2 up to current_number
        for potential_factor in range(2, original_number):
            # Step 6: Determine if potential_factor is a divisor of current_number
            if current_number % potential_factor == 0:
                # Step 7: If it is a divisor, increment the prime factors counter
                prime_factor_counter += 1
                
                # Step 8: Divide current number by potential_factor as long as it is still divisible
                while current_number % potential_factor == 0:
                    current_number //= potential_factor

        # Step 9: Check if the number has exactly two prime factors
        if prime_factor_counter == 2:
            # Step 10: If yes, increment the overall prime factor count
            prime_factor_count += 1

    # Step 11: Output the count of numbers with exactly two prime factors
    print(prime_factor_count)

# Call the function to execute
count_numbers_with_two_prime_factors()
