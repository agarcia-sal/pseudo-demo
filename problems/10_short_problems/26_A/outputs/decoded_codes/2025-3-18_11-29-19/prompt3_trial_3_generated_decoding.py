def count_special_numbers():
    # Step 1: Read an integer input from the user representing the limit
    input_limit = int(input())

    # Step 2: Initialize a variable to count the number of special numbers
    special_number_count = 0

    # Step 3: Loop through each integer from 1 to the input limit (inclusive)
    for current_number in range(1, input_limit + 1):
        # Initialize a counter for the distinct prime factors of the current number
        distinct_prime_factor_count = 0
        remaining_number = current_number

        # Step 4: Check for prime factors starting from 2 up to one less than the current number
        for potential_factor in range(2, current_number):
            # Step 5: Determine if potential_factor is a factor of remaining_number
            if remaining_number % potential_factor == 0:
                # Increment the count of distinct prime factors
                distinct_prime_factor_count += 1

                # Step 6: Divide remaining_number by potential_factor until it is no longer divisible
                while remaining_number % potential_factor == 0:
                    remaining_number //= potential_factor

        # Step 7: Check if there were exactly two distinct prime factors
        if distinct_prime_factor_count == 2:
            # Increment the special number count
            special_number_count += 1

    # Step 8: Output the total count of special numbers found
    print(special_number_count)

# To run the function:
count_special_numbers()
