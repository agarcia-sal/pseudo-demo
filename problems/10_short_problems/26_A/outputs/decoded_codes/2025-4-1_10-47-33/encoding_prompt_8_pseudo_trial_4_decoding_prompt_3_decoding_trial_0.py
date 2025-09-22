def count_product_of_two_primes():
    # Step 2: Get Input
    total_numbers = int(input())  # Read an integer value from the user

    # Step 3: Initialize Count
    result = 0  # This will count how many numbers are products of exactly two primes

    # Step 4: Iterate Through Numbers
    for current_number in range(1, total_numbers + 1):
        prime_factor_count = 0  # Count for distinct prime factors
        temp_number = current_number  # Working variable

        # Step 5: Check for Prime Factors
        for potential_factor in range(2, current_number):
            # Check if potential_factor is a factor of temp_number
            if temp_number % potential_factor == 0:
                # Found a new prime factor
                prime_factor_count += 1

                # Remove all occurrences of this factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        # Step 6: Evaluate Condition
        if prime_factor_count == 2:
            result += 1  # Found a number that is the product of exactly two primes

    # Step 7: Output the Result
    print(result)

# Running the function to execute the program
count_product_of_two_primes()
