def count_special_numbers():
    # Step 1: Read an integer t that indicates the upper limit
    t = int(input())

    # Step 2: Initialize resultCount to 0
    result_count = 0

    # Step 3: Process each number from 1 to t
    for current_number in range(1, t + 1):
        # Initialize factorCount to 0 for distinct prime factors
        factor_count = 0
        temp_number = current_number

        # Step 4: Find prime factors
        for potential_factor in range(2, current_number):
            if temp_number % potential_factor == 0:  # Check divisibility
                factor_count += 1  # Found a new prime factor
                # Continue dividing temp_number by potential_factor
                while temp_number % potential_factor == 0:
                    temp_number //= potential_factor

        # Step 5: Check if there are exactly two distinct prime factors
        if factor_count == 2:
            result_count += 1  # Increment the count of special numbers

    # Step 6: Output the total count of special numbers found
    print(result_count)

# Call the function to execute
count_special_numbers()
